import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import ast
import torch
from aimino.aimino import ProteinStructureModel # potentially unnecessary

app = Flask(__name__)

upload_folder = r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\test'
allowed_extensions = {'pdb', 'cif'}
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['SECRET_KEY'] = 'manifestninetyninepointninefive'

search_dict_path = r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\training_data\test_fasta_dict.txt'
with open(search_dict_path, 'r') as f:
    search_dict = ast.literal_eval(f.read())
test_dataset = torch.load(r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\training_data\final_test_dataset.pt', map_location=torch.device('cpu'))
test_dict = {sample[0]: sample for sample in test_dataset} # list comprehension :)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions
        
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
            return redirect(url_for('model', name=filename))
    return render_template('upload.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # LIVE SEARCH BAR
    return(render_template('search.html'))
        

@app.route('/model')
def model():
    name = request.args.get('name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(file_path, 'r') as pdb_file:
        pdb_data = pdb_file.read()
    return render_template('plot.html', pdb_data=pdb_data)

if __name__ == '__main__':
    app.run(debug=True)
    