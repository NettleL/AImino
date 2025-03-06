from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('protein_viewer.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    pass

if __name__ == '__main__':
    app.run(debug=True)
    
    