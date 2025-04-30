import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import py3Dmol

app = Flask(__name__)

upload_folder = 'SE Project - Nethya Liyanage/test'
allowed_extensions = {'pdb', 'cif'}
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['SECRET_KEY'] = 'manifestninetyninepointninefive'

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

@app.route('/model')
def model():
    name = request.args.get('name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(file_path, 'r') as pdb_file:
        pdb_data = pdb_file.read()
    return render_template('plot.html', pdb_data=pdb_data)

if __name__ == '__main__':
    app.run(debug=True)
    