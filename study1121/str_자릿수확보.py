su = 7342

print(str(su).rjust(10))    # 10자리 오른쪽 정렬
print(str(su).zfill(10))


print('|{}|'.format(su))
print('|{:0>10}|'.format(su))   # 10자리 오른쪽 정렬 남은공간 0으로 채우기
print('|{:*^10}|'.format(su))   # 10자리 가운데 정렬 남은공간 *으로 채우기
print('|{:*<10}|'.format(su))   # 10자리 왼쪽 정렬 남은공간 *으로 채우기