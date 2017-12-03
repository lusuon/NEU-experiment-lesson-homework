month=20
a,b=1,1
for i in range(month+1):
    a,b=b,b+a
    print('Month',i,':',b,"rabbits")

