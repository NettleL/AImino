
import torch
import torch.nn as nn
import torch.nn.functional as F


# NOTES
# B is batch size
# L is sequence length
# F is feature dimension
# C is channel no.



# ===================================================================
# 1. Recurrent Backbone Module
#    - with batch normalisation, GRU, residual connections & dropout
# ===================================================================
class RecurrentBackbone(nn.Module):
    def __init__(self, input_dim, hidden_dim=16, num_layers=3, dropout_rate=0.1):
        super().__init__()
        self.num_layers = num_layers
        
        # Lists to hold layers
        self.gru_layers = nn.ModuleList()
        self.bn_layers = nn.ModuleList()
        self.residual_proj = nn.ModuleList()
        self.dropout = nn.Dropout(dropout_rate)
        
        # Create each GRU layer (3)
        for i in range(num_layers):
            # First layer uses input_dim - subsequent layers use hidden_dim x 2 (bidirectionality)
            if i == 0:
                in_dim = input_dim
            else:
                in_dim = hidden_dim * 2
                
            gru_layer = nn.GRU(
                input_size=in_dim,
                hidden_size=hidden_dim,
                num_layers=1,
                batch_first=True,
                bidirectional=True
            )

            self.gru_layers.append(gru_layer)
            
            # BatchNorm1d along feature dimension
            bn_layer = nn.BatchNorm1d(in_dim)
            self.bn_layers.append(bn_layer)
            
            # If dimensions don't match the GRU output (hidden_dim*2), projection layer added
            if in_dim != hidden_dim * 2:
                proj = nn.Linear(in_dim, hidden_dim * 2)
                self.residual_proj.append(proj)
            else:
                self.residual_proj.append(nn.Identity()) # returns input unchanged
    
    def forward(self, x):
        # x: (B, L, F)
        for i in range(self.num_layers):
            # Permute to (B, F, L) for BatchNorm1d & then revert
            x_perm = x.permute(0, 2, 1)
            x_norm = self.bn_layers[i](x_perm)
            x_norm = x_norm.permute(0, 2, 1)
            
            # Process through the GRU layer.
            out, _ = self.gru_layers[i](x_norm)
            out = self.dropout(out)
            
            # Apply residual connection
            res = self.residual_proj[i](x)
            x = out + res
        return x

# ===================================================
# 2. Low-Rank Self-Attention Module
#    - Computes a scaled dot-product attention
#    - Learnable query, key, & value projections
# ===================================================
class LowRankSelfAttention(nn.Module):
    def __init__(self, embed_dim, low_rank_dim=16, dropout_rate=0.1):
        super().__init__()
        self.q_proj = nn.Linear(embed_dim, low_rank_dim)
        self.k_proj = nn.Linear(embed_dim, low_rank_dim)
        self.v_proj = nn.Linear(embed_dim, low_rank_dim)
        self.out_proj = nn.Linear(low_rank_dim, embed_dim)
        self.dropout = nn.Dropout(dropout_rate)
        self.scale = low_rank_dim ** -0.5

    def forward(self, x):
        # x: (B, L, embed_dim)
        Q = self.q_proj(x)  # (B, L, low_rank_dim)
        K = self.k_proj(x)  # (B, L, low_rank_dim)
        V = self.v_proj(x)  # (B, L, low_rank_dim)
        
        # Compute attention scores with scaling.
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale  # (B, L, L)
        attn_probs = F.softmax(attn_scores, dim=-1)
        attn_probs = self.dropout(attn_probs)
        attn_output = torch.matmul(attn_probs, V)  # (B, L, low_rank_dim)
        out = self.out_proj(attn_output)           # (B, L, embed_dim)
        return out

# ===============================================================================
# 3. Mini Transformer Block (lightweight)
#    - Single-head self-attention + feed-forward block with residual connections
# ===============================================================================
class MiniTransformerBlock(nn.Module):
    def __init__(self, embed_dim, dropout_rate=0.1, ff_hidden_dim=32):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim, num_heads=1, dropout=dropout_rate, batch_first=True)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.ff = nn.Sequential(
            nn.Linear(embed_dim, ff_hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(ff_hidden_dim, embed_dim),
            nn.Dropout(dropout_rate)
        )
        self.norm2 = nn.LayerNorm(embed_dim)
        
    def forward(self, x):
        # x: (B, L, embed_dim)
        attn_out, _ = self.attn(x, x, x)
        x = self.norm1(x + attn_out)
        ff_out = self.ff(x)
        x = self.norm2(x + ff_out)
        return x

# =============================================================
# 4.5. Linear Attention Module (for Pairwise Projection Module)
#      - Computes linear attention
# =============================================================
class LinearAttention(nn.Module):
    def __init__(self, embed_dim, dropout_rate=0.1, eps=1e-6):
        super().__init__()
        self.dropout = nn.Dropout(dropout_rate) # dropout - prevents overfitting
        self.eps = eps # small constant - ensures numerical stability (no NANs)

    def forward(self, Q, K, V):
        # Q, K, V has shape (B, N, embed_dim)
        phi = lambda x: F.elu(x) + 1  # Feature map (instead of softmax) - memory efficient

        # Apply feature map to queries _ keys
        Q_phi = phi(Q)  # (B, N, embed_dim)
        K_phi = phi(K)  # (B, N, embed_dim)
        
        # Compute denominator for normalisation
        K_sum = K_phi.sum(dim=1)  # (B, embed_dim)

        # Compute normalisation factor (dot product of transformed queries) - stable attention scaling
        Z = torch.einsum("bnd,bd->bn", Q_phi, K_sum) + self.eps  # (B, N)
        
        # Numerator - compress K and V together
        KV = torch.einsum("bnd,bne->bde", K_phi, V)  # (B, embed_dim, value_dim) where value_dim == embed_dim in our usage.
        
        # Compute attention context + apply linear projection
        context = torch.einsum("bnd,bde->bne", Q_phi, KV)  # (B, N, embed_dim)
        
        # Normalise xontext by dividing by denominator
        out = context / Z.unsqueeze(-1)  # (B, N, embed_dim)
        
        return self.dropout(out)


# ============================================================================
# 4. Pairwise Projection Module
#    - Constructs pairwise representation from sequential features
#    - Refines representation using 1x1 convolution + self-attention
# ============================================================================

class PairwiseProjectionModule(nn.Module):
    def __init__(self, seq_embed_dim, out_channels=32, dropout_rate=0.05):
        super().__init__()
        self.conv1x1 = nn.Conv2d(seq_embed_dim, out_channels, kernel_size=1)
        self.dropout = nn.Dropout(dropout_rate) # prevent overfitting
        self.attn = LinearAttention(embed_dim=out_channels, dropout_rate=dropout_rate) # Linear Attention Module
        self.norm = nn.LayerNorm(out_channels)
        self.scale_factor = nn.Parameter(torch.tensor(1.0)) # learnable scale factor
        
    def forward(self, x):
        # x has shape (B, L, seq_embed_dim)
        B, L, D = x.size()
        x_fp32 = x.float() # for better numerical stability (prevent NAN)
        
        # Creates pairwise representation
        pairwise = x_fp32.unsqueeze(2) * x_fp32.unsqueeze(1) # (B, L, L, D)
        
        # Scale by learnable factor
        pairwise = self.scale_factor * pairwise 
        
        # Rearrange tensor dimension for convolution: (B, D, L, L) (channels first)
        pairwise = pairwise.permute(0, 3, 1, 2)
        
        # Extract convolution weights in FP32
        conv_weight = self.conv1x1.weight.float()
        
        if self.conv1x1.bias is not None:
            conv_bias = self.conv1x1.bias.float()
        else:
            conv_bias = None

        # Apply convolution
        pairwise = F.conv2d(
            pairwise,
            conv_weight,
            conv_bias,
            stride=self.conv1x1.stride,
            padding=self.conv1x1.padding,
            dilation=self.conv1x1.dilation,
            groups=self.conv1x1.groups
        )
        
        pairwise = self.dropout(pairwise)
        
        # Flattens dimensions to apply linear attention
        pairwise_flat = pairwise.flatten(2).transpose(1, 2) # (B, L*L, out_channels)
        
        # Run attention
        attn_out = self.attn(pairwise_flat, pairwise_flat, pairwise_flat)
        attn_out = attn_out.float()  # Ensures FP32.
        
        # Extracts layer normalisation weights in FP32
        norm_weight = self.norm.weight.float()
        if self.norm.bias is not None:
            norm_bias = self.norm.bias.float()
        else:
            norm_bias = None

        # Apply layer normalisation
        pairwise_flat = F.layer_norm(
            pairwise_flat + attn_out,
            self.norm.normalized_shape,
            norm_weight,
            norm_bias,
            self.norm.eps
        )
        
        pairwise = pairwise_flat.transpose(1, 2).reshape(B, L, L, -1)

        # Enforce symmetry (averages matrix with its transpose)
        pairwise = 0.5 * (pairwise + pairwise.transpose(1, 2))
        
        if x.dtype == torch.half: # if original input in FP16 - convert back to FP16
            pairwise = pairwise.half()
        return pairwise

# ================================================================
# 5. Iterative Refinement Module
#    - Refines pairwise feature map
#    - Feed-forward network with residual connections
# ================================================================
class IterativeRefinementModule(nn.Module):
    def __init__(self, in_channels, ff_hidden_dim=64, dropout_rate=0.1):
        super().__init__()
        self.norm = nn.LayerNorm(in_channels)
        self.ff = nn.Sequential(
            nn.Linear(in_channels, ff_hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(ff_hidden_dim, in_channels),
            nn.Dropout(dropout_rate)
        )
    
    def forward(self, x):
        # x has shape (B, L, L, C)
        B, L, L, C = x.size()
        x_flat = x.view(B, L * L, C)
        x_norm = self.norm(x_flat)
        out = self.ff(x_norm)
        x_flat = x_flat + out

        # Reshape back to the 2D representation
        x_out = x_flat.view(B, L, L, C)
        
        # Enforce symmetry (averages matrix with its transpose)
        x_sym = 0.5 * (x_out + x_out.transpose(1, 2))
        
        return x_sym

# =================================================================================
# 6. Output Regression Module
#    - Maps refined pairwise features to distance map using 1x1 convolution
# =================================================================================
class OutputRegressionModule(nn.Module):
    def __init__(self, in_channels, dropout_rate=0.05):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, 1, kernel_size=1)
        self.dropout = nn.Dropout(dropout_rate)
        self.gain = nn.Parameter(torch.tensor(1.0)) # learnable scale factor
        
    def forward(self, x):
        # x has shape (B, L, L, C)
        B, L, L, C = x.size()
        x = x.permute(0, 3, 1, 2) # Rearrange to (B, C, L, L) for convolution
        x = self.dropout(x)
        dist_map = self.conv(x) # applies 1 x 1 convolution
                                # (B, 1, L, L)
        
        gain = torch.sigmoid(self.gain) # Multiply by learnable gain - amplifies signal
        dist_map = gain * dist_map

        # Removes dimension 1
        dist_map = dist_map.squeeze(1)  # (B, L, L)
        
        dist_map = F.softplus(dist_map) # applys softplus activation - ensures non-negative output
        
        dist_map = torch.clamp(dist_map, max=100.0) # clip very large values to avoid instability.

        dist_map = torch.sigmoid(dist_map) # applies sigmoid activation - scales values between 0-1
        
        # Enforce Symmetry
        dist_map = 0.5 * (dist_map + dist_map.transpose(1, 2))
        
        # Enforces a blacked-out (zero) diagonal (where residue L1 = L2)
        idx = torch.arange(L, device=dist_map.device)
        dist_map[:, idx, idx] = 0.0
        
        return dist_map

# ================================================================
# 7. Differentiable MDS Module
#    - Converts a 2D distance map into 3D coordinates via classical multidimensional scaling.
#    - Uses eigen-decomposition (all operations are differentiable).
# ================================================================
class DifferentiableMDSModule(nn.Module):
    def __init__(self, num_components=3, init_jitter=1e-3, max_jitter=1e-0, max_attempts=10):
        # Note - faced issue with NAN - resolved using jitter
        super().__init__()
        self.num_components = num_components # output dimensions
        self.init_jitter = init_jitter
        self.max_jitter = max_jitter # max jitter allowed
        self.max_attempts = max_attempts # max number of jitter increases

    def forward(self, dist_map, mask):
        # dist_map has shape (B, L, L)
        # mask has shape (B, L) (1 for valid, 0 for padded)

        # Force computation in FP32 (stability)
        dist_map = dist_map.float()
        # Clip the distance values
        dist_map = torch.clamp(dist_map, min=0.0, max=100.0)
        
        B, L, _ = dist_map.shape
        outputs = [] # stores embeddings
        device = dist_map.device # for tensor operations

        for b in range(B): # batches
            valid_idx = (mask[b] > 0).nonzero(as_tuple=False).squeeze().long() # get indices of valid positions.
            if valid_idx.ndim == 0: # ensure valid indices are properly shaped
                valid_idx = valid_idx.unsqueeze(0)
            L_valid = valid_idx.numel() # no. of valid elements

            if L_valid == 0:
                outputs.append(torch.zeros(L, self.num_components, device=device)) # return 0 embeddings
                continue

            # Extract distance matrix for valid entries
            d_valid = dist_map[b][valid_idx][:, valid_idx]
            # Add a small epsilon to avoid zeros (prevents issues)
            d2_valid = d_valid ** 2 + 1e-6

            # Create centering matrix for valid data
            I_valid = torch.eye(L_valid, device=device, dtype=torch.float32)
            ones_valid = torch.ones((L_valid, L_valid), device=device, dtype=torch.float32)
            J_valid = I_valid - ones_valid / L_valid

            # Compute Gram matrix
            B_mat = -0.5 * torch.mm(torch.mm(J_valid, d2_valid), J_valid)

            # Jitter and eigen-decomposition (adaptive)
            current_jitter = self.init_jitter
            attempt = 0
            success = False
            while attempt < self.max_attempts and not success:
                jitter_mat = current_jitter * I_valid
                B_jittered = B_mat + jitter_mat
                try:
                    e, v = torch.linalg.eigh(B_jittered)
                    success = True
                except RuntimeError as err:
                    attempt += 1
                    current_jitter *= 10
                    if current_jitter > self.max_jitter:
                        break

            if not success:
                # If eigen-decomposition still fails, use zeros.
                X_valid = torch.zeros((L_valid, self.num_components), device=device)
            else:
                # Select the top eigenvalues and eigenvectors.
                e_top = e[-self.num_components:]
                v_top = v[:, -self.num_components:] 
                e_top_clamped = torch.clamp(e_top, min=0)
                
                # Compute coordinates: each column scaled by the square root of the eigenvalue
                X_valid = v_top * torch.sqrt(e_top_clamped).unsqueeze(0)
            
            # Creates final output filling valid positions
            X_full = torch.zeros((L, self.num_components), device=device)
            X_full[valid_idx] = X_valid
            outputs.append(X_full)

        return torch.stack(outputs, dim=0)  # stacks processed batches - (B, L, num_components)

# ==========================================
# 8. Protein Structure Model
#    - Combines modules into a single model
# ==========================================
class ProteinStructureModel(nn.Module):
    def __init__(self, input_dim, gru_hidden_dim=16, low_rank_dim=16, pairwise_channels=32, dropout_rate=0.1):
        super().__init__()
        # Recurrent backbone (extracts sequental features)
        self.backbone = RecurrentBackbone(input_dim, hidden_dim=gru_hidden_dim, num_layers=3, dropout_rate=dropout_rate)
        backbone_dim = gru_hidden_dim * 2  # due to bidirectionality.
        
        # Low-rank self-attention (improve global context)
        self.low_rank_attention = LowRankSelfAttention(embed_dim=backbone_dim, low_rank_dim=low_rank_dim, dropout_rate=dropout_rate)
        # Mini transformer block (additional sequence-level modeling)
        self.mini_transformer = MiniTransformerBlock(embed_dim=backbone_dim, dropout_rate=dropout_rate)
        # Pairwise projection module (converts sequential embeddings into 2D features)
        self.pairwise_projection = PairwiseProjectionModule(seq_embed_dim=backbone_dim, out_channels=pairwise_channels, dropout_rate=dropout_rate)
        # Iterative refinement module (processing pairwise features)
        self.iterative_refinement = IterativeRefinementModule(in_channels=pairwise_channels, dropout_rate=dropout_rate)
        # Output regression module (maps features to a 2D distance map)
        self.output_regression = OutputRegressionModule(in_channels=pairwise_channels, dropout_rate=dropout_rate)
        # Differentiable MDS module (converts distance map to 3D coordinates)
        self.mds = DifferentiableMDSModule(num_components=3)
        
    def forward(self, x, mask=None): # if no mask provided, all positions valid
        # Input x has shape (B, L, F)
        
        seq_embed = self.backbone(x)  # (B, L, backbone_dim)
        seq_embed = seq_embed + self.low_rank_attention(seq_embed)
        seq_embed = seq_embed + self.mini_transformer(seq_embed)
        pairwise_features = self.pairwise_projection(seq_embed)  # (B, L, L, pairwise_channels)
        pairwise_features = self.iterative_refinement(pairwise_features)
        dist_map = self.output_regression(pairwise_features)     # (B, L, L)
    
        if mask is not None:
            mask2d = mask.float().unsqueeze(1) * mask.float().unsqueeze(2) # Converts mask to float + create outer product to get a (B, L, L) mask
            dist_map = dist_map * mask2d
            coords = self.mds(dist_map, mask)  # Modified MDS with mask
        else:
            coords = self.mds(dist_map, torch.ones(x.size(0), x.size(1), device=x.device, dtype=torch.bool))
        return dist_map, coords

