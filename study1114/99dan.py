
dan = 0
try:
    dan = int(input('원하는 단(1~5단) 입력>>>'))
    if dan > 5:
        raise ValueError
    
    for i in range(1, 10, 1):
        mul = dan * i
        print('%d * %d = %d' %(dan, i, mul))

except:
    print("1~5 사이 입력하라고 했잖아요.")

