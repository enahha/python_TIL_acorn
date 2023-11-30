import time

try:
    su1 = int(input('su1>>>>'))
    su2 = int(input('su2>>>>'))
    hap = su1 + su2
except Exception as ex:
    pass
    print('에러이유', ex)

print()
time.sleep(3)
print('합 = ', hap)


