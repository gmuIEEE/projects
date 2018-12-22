#import tensorflow as tf
#from tensorflow.python.keras import layers
#from sklearn.model_selection import train_test_split
#from sklearn.metric import confusion_matrix
#from sklearn.preprocessing import MinMaxScaler, normalize, OneHotEncoder

import pandas as pd
import numpy as np
import os
import cv2
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder
import pickle as p

class Data():

	def __init__(self, directory):
		self.data = {}
		self.labels = np.array([], dtype=np.str)
		self.datasize=0
		self.directory = directory
		self.height=0
		self.width=0
		self.channel=3

	def load_data(self):

		self.update_size()
		self.update_labels()
		print("Finished Initialization")
		paths = []
		labels = []
		for roots, dir, files in os.walk(self.directory):
			label = os.path.basename(roots)

			for j in files:
				path = roots + "/" + j
				path.strip()
				try:
					labels.append(label)
					paths.append(path)
				except:
					print(path, " has raised a loading error.")
					continue
		filenames = tf.constant(paths)
		labels = tf.constant(labels)
		dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
		dataset = dataset.map(self._parse_function)
		self.data = dataset

	def _parse_function(self, filename, label):
		image_string = tf.read_file(filename)
		image_decoded = tf.image.decode_jpeg(image_string)
		image_resized = tf.image.resize_images(image_decoded, [self.width, self.height])
		return image_resized, label


	def update_size(self):
		temp = 0
		for roots, dir, files in os.walk(self.directory):
			for j in files:
				path = roots + "/" + j
				path.strip()
				try:
					img = cv2.imread(path)
					#FIXME: Size is just max.
					if (temp < img.size):
						temp = img.size
						self.height,self.width, self.channel = img.shape
				except:
					print(path, " has raised a sizing error.")
					continue
		self.datasize = temp

	def get_data(self):
		return self.data

	def update_labels(self):
		for roots, dir, files in os.walk(self.directory):
			self.labels = np.append(self.labels, [os.path.basename(roots)], axis=0)


def main():
	d = Data("101_ObjectCategories")
	d.load_data()
	print(d.get_data())

main()