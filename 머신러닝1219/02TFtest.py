import tensorflow as tf

# 문자 - 영문,한글
msg = tf.constant('hello 홍길동 hong gil dong') #create a tensor생성
print( '출력 ' , msg )
print( '출력 ' , msg.numpy() ) # b'hello hong gil dong'  b=byte타입 
print( '출력 ' , msg.numpy().decode('utf-8') ) #  hello 홍길동 hong gil dong

print()
print()
print('- ' * 50) 