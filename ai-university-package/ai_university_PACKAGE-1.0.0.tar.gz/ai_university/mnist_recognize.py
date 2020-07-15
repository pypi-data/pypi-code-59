from tensorflow.keras.datasets import mnist #Библиотека с базой Mnist
from tensorflow.keras.models import Sequential # Подлючаем класс создания модели Sequential
from tensorflow.keras.layers import Dense # Подключаем класс Dense - полносвязный слой
from tensorflow.keras.optimizers import Adam # Подключаем оптимизатор Adam
from tensorflow.keras import utils #Утилиты для to_categorical
from tensorflow.keras.preprocessing import image #Для отрисовки изображения
import numpy as np # Подключаем библиотеку numpy
import pylab # Модуль для построения графиков
from mpl_toolkits.mplot3d import Axes3D # Модуль для трехмерной графики
from google.colab import files #Для загрузки своей картинки
import matplotlib.pyplot as plt #Отрисовка изображений
from PIL import Image #Отрисовка изображений
from IPython.display import clear_output
from tensorflow.keras.callbacks import LambdaCallback

class MNIST_worker:
	def __init__(self):
		self.x_train_org = []
		self.y_train_org = []
		self.x_test_org = []
		self.y_test_org = []		
		self.x_train = []
		self.x_test = []
		self.y_train = []
		self.y_test = []
		self.model = Sequential()
		
	def load_data(self):
		(self.x_train_org, self.y_train_org), (self.x_test_org, self.y_test_org) = mnist.load_data()
		clear_output(wait=True)
		print('Загружены изображения рукописных цифр')
		
	def samples(self):		
		f,ax = plt.subplots(3,10, figsize=(20,6), gridspec_kw={'wspace':.1, 'hspace':0})
		for i in range (10):
			for j in range(3):
				x_temp = self.x_train_org[self.y_train_org == i]
				img = x_temp[np.random.randint(0, x_temp.shape[0])]
				ax[j, i].imshow(img, cmap='gray')
				ax[j, i].axis('off')
		plt.show()
	
	def preproccess_images(self):
		self.x_train = self.x_train_org.reshape(60000, 784)
		self.x_test = self.x_test_org.reshape(10000, 784)
		#Нормализуем входные картинки
		self.x_train = self.x_train.astype('float32') # преобразовываем x_train в тип float (цифры с плавающей точкой)
		self.x_train = self.x_train / 255 # делим на 255, чтобы диапазон был от 0 до 1
		self.x_test = self.x_test.astype('float32') # преобразовываем x_test в тип float (цифры с плавающей точкой)
		self.x_test = self.x_test / 255 # делим на 255, чтобы диапазон был от 0 до 1
		# Преобразуем ответы в формат one_hot_encoding
		self.y_train = utils.to_categorical(self.y_train_org, 10)
		self.y_test = utils.to_categorical(self.y_test_org, 10)
		print('Созданы обучающая и проверочная выборки')
	
	def dataset_shapes(self):
		print('Размерность обучающей выборки  x_train:', self.x_train.shape)
		print('Размерность проверочной выборки x_test:', self.x_test.shape)
		print('Размерность y_train:', self.y_train.shape)
		print('Размерность  y_test:', self.y_test.shape)
		
	def create_model(self):    
		self.model.add(Dense(800, input_dim=784, activation="relu")) # Добавляем полносвязный слой на 800 нейронов с relu-активацией
		self.model.add(Dense(400, activation="relu")) # Добавляем полносвязный слой на 400 нейронов с relu-активацией
		self.model.add(Dense(10, activation="softmax")) # Добавляем полносвязный слой на 10 нейронов с softmax-активацией
		print('Создана модель нейронной сети.')
		print('Схема созданной модели:')
		self.model.summary()
	
	def set_model(self, model):
		self.model = model
		
	def train_model(self, batch_size, epochs, val_split):
		acc = []
		val_acc = []
		def on_epoch_end(epoch, log):
			count = 2
			if epoch >= 9:
				count = 1
			if epoch >= 99: 
				count = 0
			s = "* Эпоха:" + str(epoch+1) + ' '* count
			s += " | Точность (обучающая выборка): " + str(round(log['accuracy'] * 100, 2)) + '%'			
			l = len(s)
			s += ' ' * (55 - l) + "Точность (проверочная выборка): " + str(round(log['val_accuracy']* 100 ,2)) + '%'
			acc.append(log['accuracy'])
			val_acc.append(log['val_accuracy'])
			print(s)
		
		mnist_cb = LambdaCallback(on_epoch_end=on_epoch_end)		
		self.model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
		self.model.fit(self.x_train, self.y_train, batch_size=batch_size, epochs = epochs, validation_split=val_split, callbacks=[mnist_cb], verbose=0)
		plt.plot(acc, label = 'Обучающая выборка')
		plt.plot(val_acc, label = 'Проверочная выборка')
		plt.title('График точности')
		plt.xlabel('Эпоха')
		plt.ylabel('Точность')
		plt.legend()
		plt.show()
		
	def predict(self, *args):
		for i in args:
			x_temp = self.x_test[self.y_test_org == i]
			idx = np.random.randint(0, x_temp.shape[0])
			plt.imshow(x_temp[idx].reshape(28,28), cmap='gray')
			sample = np.expand_dims(x_temp[idx], 0)
			predict = self.model.predict(sample)[0]
			plt.axis('off')
			plt.show()
			print('Модель распознала цифру:', np.argmax(predict), round(max(predict)*100,2),'%')
			print()
			print()
			print()
	
	def predict_from_file(self, filename, color_inverse):
		f = image.load_img(filename, target_size=(28,28), color_mode = 'grayscale')    
		sample = np.array(f)
		plt.imshow(sample, cmap='gray')
		plt.axis('off')
		plt.show()
		sample = np.reshape(sample, (-1, 784))
		sample = sample.astype('float32')
		if color_inverse:
			sample = 255 - sample
		sample /= 255    			
		predict = self.model.predict(sample)[0]
		print('Модель распознала цифру:', np.argmax(predict), round(max(predict)*100,2),'%')	
		
		
worker = MNIST_worker()

def load_data():
	worker.load_data()
	
def samples():
	worker.samples()
def preproccess_images():
	worker.preproccess_images()
	
def dataset_shapes():
	worker.dataset_shapes()

def create_default_model():
	worker.create_model()

def set_model(model):
	worker.set_model(model)
	
def train_model(batch_size=128, epochs = 15, val_split=0.2):
	worker.train_model(batch_size, epochs, val_split)
	
def predict(*args):
	worker.predict(*args)

def predict_from_file(filename, color_inverse = False):
  worker.predict_from_file(filename, color_inverse)
	
