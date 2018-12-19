import tensorflow as tf
from tensorflow.python.keras import layers
from tensorflow.python.keras.optimizers import SGD



class LeNet5():

    def __init__(self):
        self.model = tf.keras.Sequential()
        self.epoch = 10
        self.batch_size = 100
        self.data = None
        self.learning_rate= 0.1
        self.x = None
        self.y = None
        self.one_hot_y = None
        self.loss= 0
        self.accuracy=0

    def load_data(self, data):
        self.data = data

    def build(self):

        self.model.add(layers.Conv2D(
            filters=20,
            kernel_size=(5, 5),
            padding="same",
            input_shape=(self.data.height, self.data.width, self.data.channel),
            activation= "relu"))

        self.model.add(layers.MaxPool2D(
            pool_size=(2, 2),
            strides=(2, 2)))

        self.model.add(layers.Conv2D(
            filters=50,
            kernel_size=(5, 5),
            padding="same",
            activation="relu"))

        self.model.add(layers.MaxPool2D(
            pool_size=(2, 2),
            strides=(2, 2)))

        self.model.add(layers.Flatten())

        self.model.add(layers.Dense(
            units= 500,
            activation="relu"))

        self.model.add(layers.Dense(
            units= len(data.features),
            activation = "softmax"))

        self.model.compile(
            loss="categorical_crossentropy",
            optimizer=SGD(lr=self.learning_rate),
            metrics=["accuracy"])

    def train(self):
        self.model.fit(
            train_data,
            train_labels,
            batch_size=self.batch_size,
            nb_epoch=self.epoch,
            verbose=1)

    def score(self):
        (self.loss, self.accuracy) = model.evaluate(
            test_data,
            test_labels,
            batch_size=self.batch_size,
            verbose=1)