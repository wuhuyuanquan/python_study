'''
475389urwefhjkweljfj
'''
#洗衣流程
print('输入水位；h,l')
i = input()
if i == 'h' :
   print('注水50L')
   print('搅拌30min')
   print('放水')
elif i == 'l':
    print('注水20L')
    print('搅拌10min')
    print('放水')
#甩干流程
print('输入甩干次数')
times = int(input())
for i in range (times):
   print('注水30L')
   print('搅拌20min')
   print('甩干')

