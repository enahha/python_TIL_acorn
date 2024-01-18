import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

#경고무시     
import warnings
warnings.filterwarnings('ignore') #문법의 에러나 실행중 에러가 아니라 경고무시  

num_classes = 10 # 0~9 숫자
num_features = 784 # 28*28

# Training parameters.
# learning_rate = 0.01
# training_steps = 1000
# batch_size = 256
# display_step = 50

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = np.array(x_train, np.float32), np.array(x_test, np.float32)
x_train, x_test = x_train.reshape([-1, num_features]), x_test.reshape([-1, num_features])
x_train, x_test = x_train/255., x_test/255.

train_data = tf.data.Dataset.from_tensor_slices( (x_train, y_train))
train_data =  train_data.repeat().shuffle(5000).batch(250).prefetch(1)

#가중치하고 바이어스값 지정
# rng= np.random.randn()
# print('처음실습할때 w,b난수발생해서 사용 rng ', rng)
w = tf.Variable(tf.ones([num_features, num_classes]), name='weight')
b = tf.Variable(tf.zeros([num_classes]), name='bias')

# 선형  y = x*W + b 
def logistic_regression(x):
    #def linear_regression(x):함수일때 return x*w + b
    #tf.matmul()행렬곱 https://rfriend.tistory.com/717  
    return tf.nn.softmax(tf.matmul(x, w) + b)
    

#크로스엔트로피에러 cee  113페이지 참고(밑바닥부터 시작하는 딥러닝교재 ) 
def cross_entropy(y_pred, y_true):
    y_true = tf.one_hot(y_true, depth=num_classes)
    y_pred = tf.clip_by_value(y_pred, 1e-9, 1.)
    return tf.reduce_mean(-tf.reduce_sum(y_true * tf.math.log(y_pred),1))


def my_accuracy(y_pred, y_true):
    predict = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_true, tf.int64))
    return tf.reduce_mean(tf.cast(predict, tf.float32))

# Stochastic gradient descent optimizer.
optimizer = tf.optimizers.SGD(0.01)
def run_optimizer(x, y):
    with tf.GradientTape() as g:
        pred = logistic_regression(x)
        loss = cross_entropy(pred, y)
        gs = g.gradient(loss, [w, b])
        optimizer.apply_gradients(zip(gs, [w, b]))


for step, (batch_x, batch_y) in enumerate(train_data.take(1000),1):
    run_optimizer(batch_x, batch_y) #함수호출
    if step % 5 == 0:
       pred = logistic_regression(batch_x)
       loss = cross_entropy(pred, batch_y)
       acc = my_accuracy(pred, batch_y)
       print("step: %i, loss: %f, accuracy: %f" % (step, loss, acc))


pred = logistic_regression(x_test)
print("accuracy: %f" % my_accuracy(pred, y_test))
print()
# step: 1000, loss: 0.669258, accuracy: 0.828000
# accuracy: 0.870000


test_images = x_test[:5]
predictions = logistic_regression(test_images)
for i in range(5):
    plt.imshow(np.reshape(test_images[i], [28, 28]), cmap='gray')
    plt.show()
    print("Model prediction: %i" % np.argmax(predictions.numpy()[i]))
    # Model prediction: 숫자그림출력 7 2 1 0 5
    
print()
print()
print('- ' * 50) 