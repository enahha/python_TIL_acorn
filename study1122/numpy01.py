import numpy as np
import pandas as pd

a = [2,3,4]

# numpy를 사용하지 않은 *2
for i in a:
    i * 5
    print(i, end=" ")

print()
#=====================================
# numpy array사용결과 인자 하나하나에다가  *5를 하겠다
data = np.array(a)
print(data * 5)

print(type(data))
print(data.size)    # 3
print(data.dtype)   # int64
print(data.shape)   # (3,)
