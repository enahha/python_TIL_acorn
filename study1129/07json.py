import json
import copy

my = { }
ls = []
num = 9 
path = './data/calendar.json'
data = ''

while True:
    print()
    num = int(input('1.일정등록  2.출력  9.종료 >>> '))
    if num==9:
        print('일정관리 json테스트 종료')
        break
    elif num==1:
        date = input('날짜입력 >>> ')
        am = input('오전일정 >>> ')
        pm = input('오후일정 >>> ')
        my['date'] = date
        my['am'] = am
        my['pm'] = pm
        
        with open(path, 'w', encoding='utf-8-sig') as file:
            ls.append(copy.deepcopy(my))
            json.dump(ls, file, ensure_ascii=False, indent=4)
            file.close()
        print(path , '  데이터저장 성공했습니다')

    elif num==2:
        with open('./data/calendar.json', 'r', encoding='utf-8-sig') as file2:
            data = json.load(file2)
            file2.close()
        print(data) 








print()
print('-' * 70)
