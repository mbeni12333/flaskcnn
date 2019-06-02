import os
from models.preprocess import preprocess
import torch
import matplotlib.pyplot as plt
from flask import Flask, jsonify, render_template, request

from models.KheryaNet import KheryaNet

app=Flask(__name__)

global label
label = list(range(0, 10))
label = label + [chr(ord('A')+i) for i in range(26)] + [chr(ord('a')+i) for i in range(26)]
@app.route('/')
@app.route('/index')
def index():
	return render_template('/index.html')


@app.route('/predict', methods=['POST'])
def predict():
	# retreivedata
	data=request.json
	# load model
	model = KheryaNet()
	state_dict = torch.load("models/KheryaNet32.pth", map_location="cpu")
	#print(state_dict)
	model.load_state_dict(state_dict)
	model.eval()
	# preprocess
	data=preprocess(data['data'])
	#plt.imshow(data[0].squeeze(0))
	#plt.savefig('test.png')
	data = data.transpose(0, 1, 3, 2)
	data = torch.from_numpy(data)
	# predict top k classes probabilities
	with torch.no_grad():
		out = model.forward(data)
		out = torch.exp(out)
		top_pbs , top_classes = out.topk(1, dim=1)
	print(label[top_classes[0].item()])
	d = {"class":label[top_classes[0].item()], "prob":top_pbs[0].item()}
	#dict(zip(top_classes, top_pbs))
	# encode json

	result=jsonify(d)
	# return

	return result


if __name__=="__main__":
	port=int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)
