
x = 10   # 전역변수 = global

def test():
    global x        
    x = 78
    return '금요일'

value = test()
print('전 ', x)         # 10        ||  global사용 후 = 78
print('def ', value)    # 금요일
print('후 ', x)         # 10        ||  global사용 후 = 78