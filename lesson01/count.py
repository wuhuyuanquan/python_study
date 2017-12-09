import numpy as np

#加减乘数
print('\n加减乘除')
print(1+5*4-8/2)

# 1-100求和
print('\n1-100求和')
print(sum(range(101)))

# 1-100中能够被100整除的数
print('\n1-100中能够被100整除的数')
print([i for i in range(1,101) if 100%i==0])

# 矩阵
print('\n矩阵')
print(np.mat([[2,0],[0,2]]))
      
# 逆矩阵
print('\n逆矩阵')
print(np.mat([[2,0],[0,2]]).I)
