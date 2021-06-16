import numpy as np
import random
import math
import time
import matplotlib.pyplot as plt
from pandas import DataFrame
from pandas import ExcelWriter

reveal = 0
A = []
B = []

class bit:
    def __init__(self, value, number):
        self.value = value
        self.number = number
            

    def invers(self):
            self.value = 1 - self.value

    def inverse(self, ratio):
        if random01(ratio):
            self.value = 1 - self.value

def random01(ratio):
    return int(random.random() <= ratio)

def correct_rate(Sa, Sb):
    count = 0
    for i in range(len(Sa)):
        if Sa[i].value == Sb[i].value:
            count+=1
    rate = count/len(Sa)
    return rate

def parity(s):
    sum = 0
    for i in range(len(s)):
        sum += s[i].value
    global reveal
    reveal += 1
    return sum%2

def split_half(blocka,blockb):
    l = len(blocka)
    if l == 1:
        blockb[0].invers()        
    else:        
        if parity(blocka[0:len(blocka)//2]) != parity(blockb[0:len(blocka)//2]):
            split_half(blocka[0:len(blocka)//2], blockb[0:len(blockb)//2])
        else:
            split_half(blocka[len(blocka)//2:len(blocka)], blockb[len(blocka)//2:len(blocka)])   

def split_half1(blocka,blockb,block_size):
    l = len(blocka)
    if l == 1:
        blockb[0].invers()
        n = blockb[0].number
        global A,B
        i = int(n//block_size)
        if i != math.ceil(len(A)/block_size)-1:
            if parity(A[i*block_size:i*(block_size+1)]) != parity(B[i*block_size:i*(block_size+1)]):
                split_half(A[i*block_size:i*(block_size+1)], B[i*block_size:i*(block_size+1)])
        else:
            if parity(A[i*block_size:len(A)]) != parity(B[i*block_size:len(A)]):
                split_half(A[i*block_size:len(A)], B[i*block_size:len(A)])

    else:        
        if parity(blocka[0:len(blocka)//2]) != parity(blockb[0:len(blocka)//2]):
            split_half1(blocka[0:len(blocka)//2], blockb[0:len(blockb)//2],block_size)
        else:
            split_half1(blocka[len(blocka)//2:len(blocka)], blockb[len(blocka)//2:len(blocka)],block_size)    

def compare_and_correct(Sa, Sb, block_size):
    for i in range(int(math.ceil(len(Sa)/block_size))):
        if i != math.ceil(len(Sa)/block_size)-1:
            if parity(Sa[i*block_size:(i+1)*(block_size)]) != parity(Sb[i*block_size:(i+1)*(block_size)]):
                split_half(Sa[i*block_size:(i+1)*(block_size)], Sb[i*block_size:(i+1)*(block_size)])
        else:
            if parity(Sa[i*block_size:len(Sa)]) != parity(Sb[i*block_size:len(Sa)]):
                split_half(Sa[i*block_size:len(Sa)], Sb[i*block_size:len(Sa)])

def compare_and_correct1(Sa, Sb, block_size, index_shuf):
    A_new = []
    B_new = []
    global reveal
    for j in index_shuf:
        A_new.append(Sa[j])
        B_new.append(Sb[j])
    for i in range(int(math.ceil(len(Sa)/block_size))):
        if i != math.ceil(len(Sa)/block_size)-1:
            if parity(A_new[i*block_size:(i+1)*(block_size)]) != parity(B_new[i*block_size:(i+1)*(block_size)]):                
                reveal -= 2
                split_half1(A_new[i*block_size:(i+1)*(block_size)], B_new[i*block_size:(i+1)*(block_size)],block_size)
        else:
            if parity(A_new[i*block_size:len(Sa)]) != parity(B_new[i*block_size:len(Sa)]):
                reveal -= 2
                split_half1(A_new[i*block_size:len(Sa)], B_new[i*block_size:len(Sa)],block_size)

def error_correct(size, error_rate, repeat):
    global A,B
    A = []
    B = []
    global reveal
    reveal = 0

    for i in range(size):
        r = random01(0.5)
        A.append(bit(r,i))
        B.append(bit(r,i))

    for obj in B:
        obj.inverse(error_rate)    
    
    b = 0.73
    block_size =int(math.ceil(b/error_rate))
    rate = []
    rate.append(correct_rate(A,B))
    compare_and_correct(A, B, block_size)
    rate.append(correct_rate(A,B))

    for i in range(repeat-1):   
        #block_size = block_size*2
        index_shuf = list(range(len(A)))
        random.shuffle(index_shuf)
        
        compare_and_correct1(A, B, block_size,index_shuf)
        # for obj in A:
        #     print( obj.value, end =' ' )
        # print( )
        # for obj in B:
        #     print( obj.value, end =' ' )
        # print( )
        r = correct_rate(A,B)
        rate.append(r)
        if r == 1:
            break

    keyl = len(A) - reveal/2 - 1
    if keyl < 0:
        keyl =0

    return  keyl ,rate

def error_correct_double(size, error_rate, repeat):
    global A,B
    A = []
    B = []
    global reveal
    reveal = 0

    for i in range(size):
        r = random01(0.5)
        A.append(bit(r,i))
        B.append(bit(r,i))

    for obj in B:
        obj.inverse(error_rate)    
    
    b = 0.73
    block_size =int(math.ceil(b/error_rate))
    rate = []
    rate.append(correct_rate(A,B))
    compare_and_correct(A, B, block_size)
    rate.append(correct_rate(A,B))

    for i in range(repeat-1):   
        block_size = block_size*2
        index_shuf = list(range(len(A)))
        random.shuffle(index_shuf)
        
        compare_and_correct1(A, B, block_size,index_shuf)
        # for obj in A:
        #     print( obj.value, end =' ' )
        # print( )
        # for obj in B:
        #     print( obj.value, end =' ' )
        # print( )
        r = correct_rate(A,B)
        rate.append(r)
        if r == 1:
            break

    keyl = len(A) - reveal/2 - 1
    if keyl < 0:
        keyl =0

    return  keyl ,rate


if __name__ == '__main__':

    size = 10000
    repeat = 15
    times = 100

    rate = np.zeros((25, times))
    length = np.zeros((25, times))
    sec = np.zeros((25, times))

    for j in range(25):
        for i in range(times):
            t1 = time.time()
            k ,r = error_correct_double(size, (j+1)*0.01, repeat)
            t2 = time.time()
            rate[j][i]=(len(r)-1)
            length[j][i]=k
            sec[j][i] = t2-t1

    
    df1=DataFrame(rate)
    df2=DataFrame(length)
    df3=DataFrame(sec)

    with ExcelWriter('cascade1_double.xlsx') as writer:  
        df1.to_excel(writer, sheet_name = 'iteration')
        df2.to_excel(writer, sheet_name = 'length')
        df3.to_excel(writer, sheet_name = 'time')
    
    # t2 = time.time()
    # print(t2-t1)
    # #print(keyl)
    # x = list(range(25))
    # for i in range(25):
    #     x[i] = (i+1)/100
    # plt.figure
    # l1=plt.scatter(x,rate.mean(axis=1))
    # plt.show()

    # l2=plt.scatter(x,length.mean(axis=1))
