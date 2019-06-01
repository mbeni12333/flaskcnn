import base64
from io import BytesIO
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image


class KheryaNet(nn.Module):
	instance=None

	def __init__(self):

		# initiliase the parent class
		super(KheryaNet, self).__init__()

		# define the layers

		self.conv1=nn.Conv2d(in_channels=1, out_channels=32, kernel_size=5, stride=1, padding=2, bias=True)
		self.maxpool1=nn.MaxPool2d(kernel_size=2)
		self.batchnorm1=nn.BatchNorm2d(32)
		self.conv2=nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2, bias=True)
		self.batchnorm2=nn.BatchNorm2d(64)
		self.dropout1=nn.Dropout2d(0.25)

		self.classifier=nn.Sequential(nn.Linear(12544, 128, bias=True),
		                              nn.ReLU(),
		                              nn.BatchNorm1d(128),
		                              nn.Dropout(0.5),
		                              nn.Linear(128, 62),
		                              nn.LogSoftmax(dim=1))

	def forward(self, x):

		x=F.relu(self.conv1(x))
		x=self.batchnorm1(x)
		x=F.relu(self.conv2(x))
		x=self.batchnorm2(x)
		x=self.dropout1(self.maxpool1(x))

		x=x.view(-1, 12544)

		x=self.classifier(x)

		return x

	@staticmethod
	def preprocess(data):

		data=base64.b64decode(data)
		image_data=BytesIO(data)
		img=Image.open(image_data).convert("RGB")
		img = img.resize((28, 28), Image.BICUBIC)
		#img.save("kherya","PNG")
		return data

	@staticmethod
	def getInstance(file=None):

		if KheryaNet.instance==None:
			if file:
				model=torch.load(file, map_location="cpu")
				model.eval()
			else:
				model=KheryaNet()

			KheryaNet.instance=model

		return KheryaNet.instance
