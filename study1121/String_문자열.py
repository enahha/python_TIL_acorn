msg = 'abcdefgabcebd'

# 몇번째인지 찾음
pos1 = msg.find('b')    # 1
pos2 = msg.find('b',2)  # 8
pos3 = msg.find('h')    # 없는단어 찾았을 때 = -1
pos4 = msg.index('c')   # 2     index는 찾으려는 값이 없을 경우 에러가 남
print(pos1)
print(pos2)
print(pos3)
if pos3 == -1:
    print('검색단어가 없습니다.')
print(pos4)     