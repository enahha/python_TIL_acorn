su, hap = 0, 0

while True:
    su += 1
    if su == 5: # 5일 경우에는 continue, 5를 제외하고 계산하라.
        continue
    hap = hap + su
    if su == 10:
        break
print('합계(5 제외): ', hap)
print('\n\n')

##############################
# !!! 만약 무한루프일 때 강제종료 = comm + c
##############################

su1 = 0
while True:
    su1 += 1
    print(su1 ,end='\t')
    if su1 % 5 == 0:
        print('\n')
    if su1 ==30:
        break