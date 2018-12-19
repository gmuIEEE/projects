#import tensorflow as tf
#from tensorflow.python.keras import layers
#from sklearn.model_selection import train_test_split
#from sklearn.metric import confusion_matrix
#from sklearn.preprocessing import MinMaxScaler, normalize, OneHotEncoder

import pandas as pd
import numpy as np
import os
import cv2
from sklearn.preprocessing import OneHotEncoder
import pickle as p

class Data():

	def __init__(self, directory):
		self.data = pd.DataFrame()
		self.features = np.array([], dtype=np.str)
		self.datasize=0
		self.directory = directory
		self.height=0
		self.width=0
		self.channel=3

	def load_data(self):

		self.update_size()
		self.update_features()
		print("Finished Initialization")


		for roots, dir, files in os.walk(self.directory):
			temp_data = []
			feature = os.path.basename(roots)
			for j in files:
				path = roots + "/" + j
				path.strip()
				try:
					img = cv2.imread(path)
					#print(img.size, " resizing to", self.datasize,"...")
					img = cv2.resize(img, (self.width, self.height))
					temp_data.append(img)
				except:
					print(path, " has raised a loading error.")
					continue
			self.data[feature] = pd.Series(np.array(temp_data))




	def update_size(self):
		temp = 0
		for roots, dir, files in os.walk(self.directory):
			for j in files:
				path = roots + "/" + j
				path.strip()
				try:
					img = cv2.imread(path)
					#FIXME: Size is just max.
					if (temp < img.size) and (img.size<318193):
						temp = img.size
						self.height,self.width, self.channel = img.shape
				except:
					print(path, " has raised a sizing error.")
					continue
		self.datasize = temp

	def get_data(self):
		return self.data

	def update_features(self):
		for roots, dir, files in os.walk(self.directory):
			self.features = np.append(self.features, [os.path.basename(roots)], axis=0)


def main():
	d = Data("101_ObjectCategories")
	d.load_data()
	print(d.get_data())

main()