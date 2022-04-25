from flask import Flask, jsonify
import io
import torchvision.transforms as transforms
from PIL import Image

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'class_id': 'IMAGE_NET_XXX', 'class_name': 'Cat'})