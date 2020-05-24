import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

labelsPath="yolo_v3/coco.names"
cfgpath="yolo_v3/yolov3.cfg"
wpath="yolo_v3/yolov3.weights"
Lables=get_labels(labelsPath)
CFG=get_config(cfgpath)
Weights=get_weights(wpath)
nets=load_model(CFG,Weights)
Colors=get_colors(Lables)
# Initialize the Flask application

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('/client/public/index.html')

@app.route('/api/test', methods=['POST'])
def main():
    img = request.files["image"].read()
    img = img.open(io.BytesIO(img))
    npimg = np.array
