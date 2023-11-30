
# iLIst = [2, 7, 1]
# iLIst.sort()
# print(iLIst)

a, b, c = 3, 2, 1
if (b > c):
    b, c = c, b

    if(a > b):
        a, b = b, a

        if(b>c):
            b,c = c,b
elif(b < c):
    
    if(a > b):
        a, b = b, a

        if(b>c):
            b,c = c,b

print(a,b,c)