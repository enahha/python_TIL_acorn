import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

#모델생성
from tensorflow import keras
from tensorflow.keras.layers  import  Dense, BatchNormalization, Dropout



(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)
print(train_labels.shape)
print()

print(test_images.shape)
print(test_labels.shape)
print()

# (60000, 28, 28) 훈련용 
# (60000,)

# (10000, 28, 28) 테스트용
# (10000,)

def show_images(dataset, label, nrow, ncol):
    print()
    fig,axes = plt.subplots(nrows=nrow, ncols=ncol, figsize=(2*ncol, 2*nrow))
    ax = axes.ravel()
    xlabels= label[0:nrow*ncol]
    for i in range(nrow*ncol):
        image = dataset[i]
        ax[i].imshow(image, cmap='gray')
        ax[i].set_xlabel(xlabels[i])

    plt.tight_layout()
    plt.show()

show_images(train_images,train_labels, 4, 5)
print()
print(train_images[0])

#모델생성 맨위쪽에 기술
from tensorflow import keras
from tensorflow.keras.layers  import  Dense, BatchNormalization, Dropout

#순서1] 모델생성 
model = keras.models.Sequential()
model.add( keras.layers.Flatten(input_shape=[28,28], name='input1'))
model.add(Dense(300, activation='relu', name='hidden1'))
model.add(Dense(200, activation='relu', name='hidden2'))
model.add(Dense(100, activation='relu', name='hidden3'))
model.add(Dense(10, activation='softmax', name='output'))
print(model.summary())
print('모델생성 111 222 ')

#Dense클래스는 뉴런의 입력과 출력을 연결해주는 히든레이어 



















print()
print('- ' * 70)













print()
print()
print('- ' * 50) 