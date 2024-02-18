from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

from img_to_txt import gen_txt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if 'image' not in request.files:
        print("Here")
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        text = gen_txt()
        return jsonify({'message': 'Image uploaded successfully', 'data': text}), 200

    return jsonify({'error': 'Failed to upload image'}), 500

app.run(port=8000, debug=True)