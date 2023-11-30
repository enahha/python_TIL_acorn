money = int(input('요금입력>>>'))
ment = '거스름돈 = '

while True:
    print('\n ---------- 커피 요거 프레소 -------------')
    print('1, coffee 300won     2, latte 350won     3, cocoa 400won     4, return   5, exit')
    sel = int(input('메뉴선택>>>>'))

    if (sel == 1):
        change = money - 300
        break
    elif (sel == 2):
        change = money - 350
        break
    elif (sel == 3):
        change = money - 400
        break
    elif (sel == 4):
        continue
    elif (sel == 5):
        break

print(ment, change)
