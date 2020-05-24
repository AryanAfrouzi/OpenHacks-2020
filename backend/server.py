import numpy as np
from flask import Flask, request, jsonify, render_template
from test import *

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
    image=npimg.copy()
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    res=evaluate(image,nets,Lables,Colors)
    image=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
    np_img=Image.fromarray(image)
    img_encoded=image_to_byte_array(np_img)
    return Response(response=img_encoded, status=200,mimetype="image/jpeg"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
