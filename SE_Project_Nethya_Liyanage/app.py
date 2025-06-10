import os
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import torch
import torch.nn.functional as F
import numpy as np

from aimino.aimino import ProteinStructureModel
from aimino.plot_prot import pearsons_corr_coef, plot, classical_mds
from aimino.download import create_npz_file, create_pdb_file
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))

default_upload_folder = os.path.join(basedir, 'static', 'uploads')
upload_folder = os.environ.get('UPLOAD_FOLDER', default_upload_folder)
app.config['UPLOAD_FOLDER'] = upload_folder
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
    
default_download_folder = os.path.join(basedir, 'static', 'downloads')
download_folder = os.environ.get('DOWNLOAD_FOLDER', default_download_folder)
app.config['DOWNLOAD_FOLDER'] = download_folder
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'manifestninetyninepointninefive')

allowed_extensions = {'pdb', 'cif'}

model = None

base_dir = os.path.dirname(os.path.abspath(__file__)) # where app.py is located

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_data(key):
    data_path = os.path.join(base_dir, "aimino", "final_test_dataset.pt")
    with open(data_path, "rb") as f:
        data_dict = torch.load(f, map_location="cpu")
    return next((sample for sample in data_dict if sample[0] == key), None)
def load_model_dict(): # caching 
    global model
    
    model_path = os.path.join(base_dir, "aimino", "final_trained_model_cpu.pt")
    
    try:
        model_instance = ProteinStructureModel(
            input_dim=427,
            gru_hidden_dim=16,
            low_rank_dim=16, 
            pairwise_channels=32, 
            dropout_rate=0.05929059580679108
        )
        
        state_dict = torch.load(model_path, map_location=torch.device('cpu'))
        model_instance.load_state_dict(state_dict)
        model_instance.eval()
        
        model = model_instance
        print('Model cached')
    except Exception as e:
        print('Failed to load model:', e)

load_model_dict()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename=='':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('plot_model', name=filename))
    return render_template('upload.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    return(render_template('search.html'))

@app.route('/predict', methods=['POST'])
def predict():
    global model
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid request payload"}), 400
    
    key = data.get('key', None)
    if key is None or key.strip() == '':
        return jsonify({"error": "No key provided"}), 400

    key_data = get_data(key)
    if key_data is None:
        return jsonify({"error": "Key not found in dataset"}), 400

    protein_seq, test_input, test_mask, test_target = key_data

    tensor_input = test_input.detach().clone().unsqueeze(0).float()
    tensor_mask = test_mask.detach().clone().unsqueeze(0).float()

    with torch.no_grad():
        output = model(tensor_input, tensor_mask)
        dist_ca_map_pred = output[0] if isinstance(output, tuple) else output

    tensor_target = test_target.detach().clone().unsqueeze(0).float()

    rmse = torch.sqrt(F.mse_loss(dist_ca_map_pred, tensor_target)).item()
    pearson = pearsons_corr_coef(dist_ca_map_pred, tensor_target).item()

    plot_image = plot(dist_ca_map_pred.squeeze(0).cpu().numpy(),
                      tensor_target.squeeze(0).cpu().numpy(),
                      rmse, pearson)
    
     # Calculate 3D coordinates using classical MDS
    xyz_pred = classical_mds(dist_ca_map_pred.squeeze(0).cpu().numpy())
    xyz_target = classical_mds(tensor_target.squeeze(0).cpu().numpy())

    # Use create_npz_file to generate and save the NPZ file.
    npz_filename = create_npz_file(
        dist_pred=dist_ca_map_pred.squeeze(0).cpu().numpy(),
        dist_target=tensor_target.squeeze(0).cpu().numpy(),
        xyz_pred=xyz_pred,
        xyz_target=xyz_target,
        key=key
    )
    
    # Generate the PDB file using create_pdb_file.
    pdb_string = create_pdb_file(dist_ca_map_pred.squeeze(0).cpu().numpy())
    pdb_filename = f"{key}_pred.pdb"
    pdb_path = os.path.join(app.config['DOWNLOAD_FOLDER'], pdb_filename)
    with open(pdb_path, 'w') as f:
        f.write(pdb_string)
    
    return render_template('predict.html', 
                           rmse=rmse, 
                           pearson=pearson, 
                           plot_image=plot_image,
                           pdb_filename=pdb_filename,
                           npz_filename=npz_filename)
    
@app.route('/model')
def plot_model():
    name = request.args.get('name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(file_path, 'r') as pdb_file:
        pdb_data = pdb_file.read()
    return render_template('plot.html', pdb_data=pdb_data)

if __name__ == '__main__':
    app.run(debug=True)
    