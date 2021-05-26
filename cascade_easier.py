import numpy as np
import random
import math
import time


reveal = 0

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

def compare_and_correct(Sa, Sb, block_size):
    for i in range(int(math.ceil(len(Sa)/block_size))):
        if i != math.ceil(len(Sa)/block_size)-1:
            if parity(Sa[i*block_size:i*(block_size+1)]) != parity(Sb[i*block_size:i*(block_size+1)]):
                split_half(Sa[i*block_size:i*(block_size+1)], Sb[i*block_size:i*(block_size+1)])
        else:
            if parity(Sa[i*block_size:len(Sa)]) != parity(Sb[i*block_size:len(Sa)]):
                split_half(Sa[i*block_size:len(Sa)], Sb[i*block_size:len(Sa)])

def error_correct(size, error_rate, repeat):
    
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
    # for obj in A:
    #     print( obj.value, end =' ' )
    # print( )
    # for obj in B:
    #     print( obj.value, end =' ' )
    # print( )
    b = 0.73
    block_size =int(math.ceil(b/error_rate))
    rate = []
    rate.append(correct_rate(A,B))
    compare_and_correct(A, B, block_size)
    rate.append(correct_rate(A,B))

    for i in range(repeat-1):   
        index_shuf = list(range(len(A)))
        random.shuffle(index_shuf)
        
        A_new = []
        B_new = []

        for j in index_shuf:
            A_new.append(A[j])
            B_new.append(B[j])
        compare_and_correct(A_new, B_new, block_size)
        rate.append(correct_rate(A,B))

    keyl = len(A) - reveal/2 - 1
    if keyl < 0:
        keyl =0

    return  keyl ,rate
if __name__ == '__main__':
    t1 = time.time()

    keyl = []
    rate = []
    for i in range(10):
        k ,r = error_correct(10000, 0.01, 4)
        keyl.append(k)
        rate.append(r)

    t2 = time.time()
    print(t2-t1)
    print(keyl)
    print(rate)