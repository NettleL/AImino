import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import py3Dmol

app = Flask(__name__)

upload_folder = 'SE Project - Nethya Liyanage/misc'
allowed_extensions = {'pdb', 'cif'}
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['SECRET_KEY'] = 'manifestninetyninepointninefive'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions
        
@app.route("/", methods=['GET', 'POST'])
def home():
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
        
    pdb_code = '6DT1'  # Replace with your PDB code
    viewer = py3Dmol.view(query='pdb:' + pdb_code)
    viewer.setStyle({'sphere': {'radius':0.5}})
    viewer.zoomTo()
    html = viewer._make_html()
    return render_template('home.html', home_html=html)

@app.route('/model')
def model():
    name = request.args.get('name')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(file_path, 'r') as pdb_file:
        pdb_data = pdb_file.read()
    
    viewer = py3Dmol.view(data=pdb_data, format="pdb")
    viewer.setStyle({'cartoon': {'color':'spectrum'}})
    viewer.zoomTo()
    html = viewer._make_html()
    return render_template('plot.html', plot_html=html)

if __name__ == '__main__':
    app.run(debug=True)
    
    