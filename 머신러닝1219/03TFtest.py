import tensorflow as tf

# 정수,실수 
msg = tf.constant(279) # 정수 create a tensor생성
print( '출력 ' , msg )
print( '출력 ' , msg.numpy() ) # tf.Tensor(279, shape=(), dtype=int32)  

pi = tf.constant(3.14) # 실수  a tensor생성
print( '출력 ' , pi ) # tf.Tensor(3.14, shape=(), dtype=float32) 
print( '출력 ' , pi.numpy() ) # 3.14

# 세번째  bool타입 
gender = tf.constant(True) # bool a tensor생성
print( '출력 ' , gender ) # tf.Tensor(True, shape=(), dtype=bool)
print( '출력 ' , gender.numpy() ) #True

print()
print()
print('- ' * 50) 