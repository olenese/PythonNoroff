from flask import request
from flask import Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload_file', methods =['GET', 'POST'])
def upload_file():
        if request.method == 'GET':
                return 'Method not supported for this function'
        if request.method == 'POST':
                file = request.files['cred_dump']

                if file.filename[-4:] == '.txt':
                        file.save('credentials/{}'.format(secure_filename(file.filename)))
                        return 'success'
                else:
                        return 'Error'


