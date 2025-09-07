import os
from flask import Flask, request, render_template
import boto3
from datetime import datetime

app = Flask(__name__)

# connect to S3 using credentials
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    # basic file extension check
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
# UI for file upload
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        print(f"Uploaded by Ajay Zutshi | File: {file.filename} | Time: {datetime.now()}")
        return f"Uploaded {file.filename} to S3 bucket!"
    return 'Invalid file type. Only PDF and image files are allowed.'

if __name__ == '__main__':
    app.run(debug=True)
