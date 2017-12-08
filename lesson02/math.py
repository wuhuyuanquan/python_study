'''
求 1+2+3+4...100=?
    '''
s =0
for i in range (1,101):
   s+=i
print(s)

# 2+4+6...100=?
s = 0
for i in range(1,101):
    if i % 2 == 0:
        s += i
print(s)

#
s = 0
for i in range(1,101):
    if i % 2 != 0:continue
    s += i
print(s)

#打印0-100，偶数，各个数位相加得9，
for i in range(1,101):
    if i%2==0 and i%10 + i//10 == 9:
       print(i)

#输出 偶数，各个数位相加得9 （7个）
s,i = 0,0
while True:
   i += 1
   if i%2 == 1: continue
   d,e = 0,i
   while e > 0:
       d += e%10
       e //= 10
   if d == 9:
      s += 1
      print(i)
      if s == 7 :break


