#仅能被1和它自己整除的数
for i in range(1,101):
   if i==1:
       continue
   k=0
   for j in range(2,i):
         if i%j==0:
            k=1
   if k==0:
        print(i)
        
