
# iLIst = [2, 7, 1]
# iLIst.sort()
# print(iLIst)

a, b, c = 4, 3, 6
if (b > c):
    b, c = c, b

    if(a > b):
        a, b = b, a

        if(b>c):
            b,c = c,b
else:

    if(a > b):
        a, b = b, a

        if(b>c):
            b,c = c,b

print(a,b,c)