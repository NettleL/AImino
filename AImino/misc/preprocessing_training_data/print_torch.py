import torch

data = torch.load(r'C:\Users\cgwl\Documents\AImino_Training\final_dataset_padded.pt', weights_only=False) # must keep weights_only=False - otherwise error

count = 0
for seq_id, data in data.items():
    print(f"Protein ID: {seq_id}")
    print(f"  Input shape: {data['input'].shape}")
    print(f"  Target shape: {data['target'].shape}")
    print(f"  Sequence length: {len(data['sequence'])}")
    print("-" * 40) # for the .⟡ aesthetic ⟡.
    count = count + 1
print(count)
