#斐波那契数列是以1，1开头，从第3项开始，每一项都是由前两个的和构成，请编程得到数列的前100项，并输出99项与100项的比值
a,b,i=1,1,1
c=1


print('第i项    斐波那契数列')
print(   i, '      ',  a)
i += 1
print(  i, '      ', b)

while True:
   if c % 2 != 0:
         a=a+b
         i += 1
         print(   i,  '      ',  a)
   c += 1
   if c % 2 == 0:
         b=a+b
         i += 1
         print(   i,  '      ', b)
   c +=1
   if c == 99:
      print(a,'/',b,'=',a/b)
      break

