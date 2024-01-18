import tensorflow as tf

# 텐서플로우연산
a = tf.constant(16)
b = tf.constant(3)
c = tf.constant(5)

print('합계 =' , tf.add(a,b))
print('빼기 =' , tf.subtract(a,b))
print('곱셈 =' , tf.multiply(a,b))
print('몫값 =' , tf.divide(a,b))
print()

add = tf.add(a,b)
sub = tf.subtract(a,b)
mul = tf.multiply(a,b)
div = tf.divide(a,b)
print('결과 ',  (a+b)) # tf.Tensor(19, shape=(), dtype=int32)
print('합 ',  add.numpy()) 
print('차 ',  sub.numpy()) 
print('곱 ',  mul.numpy()) 
print('몫 ',  round(div.numpy(),2)) 
print()


x = tf.constant(16)
y = tf.constant(3)
z = tf.constant(5)
mean = tf.reduce_mean([x,y,z])
sum = tf.reduce_sum([x,y,z])
print('평균 ', mean.numpy())
print('합계 ', sum.numpy())

mt1 = tf.constant( [[1., 2.] , [3., 4.] ])
mt2 = tf.constant( [[5., 6.] , [7., 8.] ])
ret3 = tf.matmul(mt1, mt2) 
print('행렬곱 ', ret3.numpy()) #[[19. 22.] [43. 50.]]

print()
print('- ' * 50) 