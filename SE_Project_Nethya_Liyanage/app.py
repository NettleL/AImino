import os
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import torch
import torch.nn.functional as F

from aimino.aimino import ProteinStructureModel
from aimino.plot import classical_mds, pearsons_corr_coef, plot
app = Flask(__name__)

upload_folder = r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\test'
allowed_extensions = {'pdb', 'cif'}
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['SECRET_KEY'] = 'manifestninetyninepointninefive'

model = None
data_dict = None

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions
       
def load_model_dict(): # caching 
    global model, data_dict
    base_dir = os.path.dirname(os.path.abspath(__file__)) # where app.py is located
    
    data_path = os.path.join(base_dir, "aimino", "final_test_dataset.pt")
    model_path = os.path.join(base_dir, "aimino", "final_trained_model_cpu.pt")
    
    try:
        data_dict = torch.load(data_path)
        print('Data dictionary cached')
    except Exception as e:
        print('Failed to load dictionary:', e)

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
    global model, data_dict
    data = request.get_json()
    key = data.get('key', None)
    if key is None or key.strip() == '':
        return jsonify({"error": "No key provided"}), 400

    if data_dict is None:
        return jsonify({"error": "Data dictionary not loaded"}), 400
    
    key_data = None
    for sample in data_dict:
        protein_seq, test_input, test_mask, test_target = sample
        if protein_seq == key:
            key_data = {
                "input": test_input,
                "mask": test_mask,
                "target": test_target
                }
            break

    if key_data is None:
        return jsonify({"error": "Key not found in dataset"}), 400

    input_data = key_data.get("input")
    ground_truth = key_data.get("target")
    
    if input_data is None or ground_truth is None:
        return jsonify({"error": "Incomplete data for key"}), 400

    if model is None:
        return jsonify({"error": "Model not loaded"}), 400
        
    try:
        if isinstance(input_data, torch.Tensor):
            tensor_input = input_data.clone().detach()
        else:
            tensor_input = torch.tensor(input_data)
        tensor_input = tensor_input.unsqueeze(0).float()
    except Exception as e:
        return jsonify({"error": f"Error converting input to tensor: {e}"}), 400
    
    try:
        if isinstance(key_data["mask"], torch.Tensor):
            tensor_mask = key_data["mask"].clone().detach()
        else:
            tensor_mask = torch.tensor(key_data["mask"])
        tensor_mask = tensor_mask.unsqueeze(0)
    except Exception as e:
        return jsonify({"error": f"Error converting mask to tensor: {e}"}), 400
    
    with torch.no_grad():
        try:
            output = model(tensor_input, tensor_mask)
            if isinstance(output, tuple):
                dist_ca_map_pred = output[0]
            else:
                dist_ca_map_pred = output
        except Exception as e:
            print("Model Prediction Error:", e) 
            return jsonify({"error": f"Error during model prediction {e}"}), 400
    try:
        if isinstance(ground_truth, torch.Tensor):
            tensor_target = ground_truth.clone().detach()
        else:
            tensor_target = torch.tensor(ground_truth)
        tensor_target = tensor_target.unsqueeze(0).float()
    except Exception as e:
        return jsonify({"error": f"Error converting target to tensor: {e}"}), 400
        
    rmse = torch.sqrt(F.mse_loss(dist_ca_map_pred, tensor_target)).item()
    pearson = pearsons_corr_coef(dist_ca_map_pred, tensor_target).item()

    pred_np = dist_ca_map_pred.squeeze(0).cpu().numpy()
    target_np = tensor_target.squeeze(0).cpu().numpy()

    plot_image = plot(pred_np, target_np, rmse, pearson)
    
    return render_template('predict.html', rmse=rmse, pearson=pearson, plot_image=plot_image)

@app.route('/model')
def plot_model():
    name = request.args.get('name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(file_path, 'r') as pdb_file:
        pdb_data = pdb_file.read()
    return render_template('plot.html', pdb_data=pdb_data)

if __name__ == '__main__':
    app.run(debug=True)
    