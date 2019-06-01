from flask import Flask, request, render_template, jsonify
from models.KheryaNet import KheryaNet
import os



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('/index.html')


@app.route('/predict', methods=['POST'])
def predict():
    #retreivedata
    data = request.json
    #load model
    model = KheryaNet.getInstance("models/KheryaNet.pth")
    #preprocess
    data_processed = KheryaNet.preprocess(data['data'])


    #predict top k classes probabilities

    #out = model.predict(data)
    #top_pbs , top_classes = out.topK(5, dim=1)



    #encode json

    result = jsonify(data)
    #return

    return result

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
