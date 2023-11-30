
score = {'김펭귄':[90,80],
         '장희빈':[86,98],
         '박딕트':[86,98],
         '김이썬':[86,98]
         }

result = 0
for i,j in enumerate(score):
    for a in range(2):
        result += score[j][a]
    print(i , '_',j, '__', score[j][0], score[j][1], 'total = ',result)

print()

# 다른 해결
tot = 0
for i, (key, data) in enumerate(score.items()):
    for a in range(2):
        tot += score[key][a]
    print(i, key, data[0], data[1], tot)