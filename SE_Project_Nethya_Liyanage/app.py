import os
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, send_from_directory, make_response
from werkzeug.utils import secure_filename
import torch
import torch.nn.functional as F
import numpy as np

from aimino.aimino import ProteinStructureModel
from aimino.plot_prot import pearsons_corr_coef, plot, classical_mds
from aimino.download import create_npz_file

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Upload Folder
default_upload_folder = os.path.join(basedir, 'static', 'uploads')
upload_folder = os.environ.get('UPLOAD_FOLDER', default_upload_folder)
app.config['UPLOAD_FOLDER'] = upload_folder
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
    
# Download Folder
default_download_folder = os.path.join(basedir, 'static', 'downloads')
download_folder = os.environ.get('DOWNLOAD_FOLDER', default_download_folder)
app.config['DOWNLOAD_FOLDER'] = download_folder
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'manifestninetyninepointninefive')

allowed_extensions = {'pdb'} # for upload - may increase to include .cif in later development

model = None

base_dir = os.path.dirname(os.path.abspath(__file__)) # where app.py is located

# Checks whether uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Gets data in data_dict - loaded like this in attempt to mitigate render issues with high memory dataset
# despite finally not using render I did not remove this - I thought it would be useful anyway
def get_data(key):
    data_path = os.path.join(base_dir, "aimino", "final_test_dataset.pt")
    with open(data_path, "rb") as f:
        data_dict = torch.load(f, map_location="cpu")
    return next((sample for sample in data_dict if sample[0] == key), None)

# Loads model & model state dictionary
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

# Home
@app.route("/")
def home():
    return render_template('home.html')

# Upload
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

# Search
@app.route('/search', methods=['GET', 'POST'])
def search():
    return(render_template('search.html'))

# Predict
@app.route('/predict', methods=['POST'])
def predict():
    global model
    data = request.get_json()
    
    # Error Messages (Just in case)
    if data is None:
        return jsonify({"error": "Invalid request payload"}), 400
    
    key = data.get('key', None)
    if key is None or key.strip() == '':
        return jsonify({"error": "No key provided"}), 400

    key_data = get_data(key)
    if key_data is None:
        return jsonify({"error": "Key not found in dataset"}), 400

    # Extract data
    protein_seq, test_input, test_mask, test_target = key_data
    tensor_input = test_input.detach().clone().unsqueeze(0).float()
    tensor_mask = test_mask.detach().clone().unsqueeze(0).float()
    
    # Model prediction
    with torch.no_grad():
        output = model(tensor_input, tensor_mask)
        dist_ca_map_pred = output[0] if isinstance(output, tuple) else output

    tensor_target = test_target.detach().clone().unsqueeze(0).float()
    
    # Compute Stats
    rmse = torch.sqrt(F.mse_loss(dist_ca_map_pred, tensor_target)).item()
    pearson = pearsons_corr_coef(dist_ca_map_pred, tensor_target).item()
    
    # Generate plot Image
    plot_image = plot(dist_ca_map_pred.squeeze(0).cpu().numpy(),
                      tensor_target.squeeze(0).cpu().numpy(),
                      rmse, pearson)
    
    # gets 3d coordinates for downloadable npz_file 
    xyz_pred = classical_mds(dist_ca_map_pred.squeeze(0).cpu().numpy())
    xyz_target = classical_mds(tensor_target.squeeze(0).cpu().numpy())
    
    # npz file
    npz_filename = create_npz_file(
        dist_pred=dist_ca_map_pred.squeeze(0).cpu().numpy(),
        dist_target=tensor_target.squeeze(0).cpu().numpy(),
        xyz_pred=xyz_pred,
        xyz_target=xyz_target,
        key=key
    )
    
    # render results
    html = render_template('predict.html', 
                           rmse=rmse, 
                           pearson=pearson, 
                           plot_image=plot_image,
                           npz_filename=npz_filename,
                           error = '')
    response = make_response(html)
    
    # controls caching behaviour - forces browser to always fetch new data
    # instead of relying on outdated cached responses (to deal with issue with npz downloads)
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0' 
    
    return response

# Download
@app.route('/download/<filename>')
def download_file(filename):
    npz_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
    if os.path.exists(npz_filepath):
        return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)
    else:
        return jsonify({"error": "File cleared. Cannot download."}), 410
        # If folder was cleared prior to attempted download
        # Note - if protein A is predicted, the user clears the folder & the user searches protein A again
        # they will be able to download the npz file (of the new prediction)

# Delete
@app.route('/delete-files',methods=['POST'])   
def delete_files():
    try:
        files = os.listdir(download_folder)
        if not files:
            return jsonify({"message": "No files to delete"}), 200

        for file in files: # Delete all files
            file_path = os.path.join(download_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        return jsonify({"message": "All files deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"Failed to delete files: {str(e)}"}), 500
 
# Plot PDB   
@app.route('/model')
def plot_model():
    name = request.args.get('name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(file_path, 'r') as pdb_file:
        pdb_data = pdb_file.read()
    return render_template('plot.html', pdb_data=pdb_data)

if __name__ == '__main__':
    app.run(debug=True)
    