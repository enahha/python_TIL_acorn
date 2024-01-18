import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


X = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
              7.042,10.791,5.313,7.997,5.654,9.27,3.1])

Y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
              2.827,3.465,1.65,2.904,2.42,2.94,1.3])


rng= np.random.randn()
print('난수 rng ', rng)
w = tf.Variable( rng, name='weight')
b = tf.Variable( rng, name='bias')


# 선형  y = x*W + b 
def linear_regression(x):
    return x*w + b

#평균제곱에러 mse
def mean_square(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))


#Stochastic Gradient Descent 경사하강법
optimizer = tf.optimizers.SGD(0.01)
def run_optimizer():
   with tf.GradientTape() as g:
       pred=linear_regression(X)
       loss = mean_square(pred, Y)
       gs = g.gradient(loss,[w,b])
       optimizer.apply_gradients(zip(gs,[w,b]))
    
      
for step in range(1,101,1):
    run_optimizer() #함수호출
    if step % 5 == 0:
        pred = linear_regression(X)
        loss = mean_square(pred, Y)
        print('step:%i  loss:%f  W:%f  b:%f' %(step, loss, w.numpy(), b.numpy()))

print('for 반복문 10회반복 처리  확인 ok ok')
print()

plt.plot(X, Y, 'ro', label='data')
plt.plot(X, np.array(w*X+b), label='line')
plt.legend()
plt.show()

print()
print('- ' * 50)