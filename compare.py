import time
import numpy as np
import matplotlib.pyplot as plt

import cascade_easier
import cascade_1
t1 = time.time()
size = 10000
repeat = 5
times = 100

rate1 = np.zeros((25, times))
rate2 = np.zeros((25, times))

for j in range(25):
    for i in range(times):
        k ,r = cascade_easier.error_correct(size, (j+1)*0.01, repeat)
        rate1[j][i]=(r.index(1))
        k ,r = cascade_1.error_correct(size, (j+1)*0.01, repeat)
        rate2[j][i]=(r.index(1))

t2 = time.time()
print(t2-t1)

x = list(range(25))
for i in range(25):
    x[i] = (i+1)/100
plt.figure
l1=plt.scatter(x,rate1.mean(axis=1))
l2=plt.scatter(x,rate2.mean(axis=1),c="red")

plt.legend(handles=[l1,l2],labels=['1','2'])
plt.show()
