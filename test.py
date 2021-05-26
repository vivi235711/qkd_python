import random
import numpy as np
import matplotlib.pyplot as plt
# class bit:
#     def __init__(self, value):
#         self.value = value

#     def inverse(self, ratio):
#         if random01(ratio):
#             self.value = 1 - self.value

# def random01(ratio):
#     if ratio == 0.5:
#         return random.randint(0, 1)
#     else:
#         return int(random.random() <= ratio)
# A = []
# B = []
# size = 10
# error_rate = 0.1
# for i in range(size):
#     r = random01(0.5)
#     A.append(bit(r))
#     B.append(bit(r))



# for obj in B:
#     obj.inverse(error_rate)

# for obj in A:
#     print( obj.value, end = ' ' )
# print( )
# for obj in B: 
#     print( obj.value, end = ' ' )
# print( )
# random.Random(4).shuffle(A)
# random.Random(4).shuffle(B)
# for obj in A:
#     print( obj.value, end = ' ' )
# print( )
# for obj in B: 
#     print( obj.value, end = ' ' )

a = np.array([[4,3,5,6,7,4],[4,5,6,9,2,6],[1,6,9,2,2,6]])
print(a.mean(axis=1))