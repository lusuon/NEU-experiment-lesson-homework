DoM = [31,28,31,30,31,30,31,31,30,31,30,31]
yy=eval(input('Enter the year'))
if yy%100==0 and yy%4!=0:
    pass
elif yy%4==0:
    DoM[1]=29
else:
    pass
mm=0
while mm not in range (1,13):
    mm=eval(input('Enter the month'))
dd=0
while dd not in range (1,DoM[mm-1]+1):
    dd=eval(input('Enter the day'))
num=0
print('''There are''',sum(DoM[0:mm-1])+dd,'day(s)')
