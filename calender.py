DoM = [31,28,31,30,31,30,31,31,30,31,30,31]
WEEK=['SUN','MON','TUE','WED','THU','FRI','SAT']
yy=eval(input('Enter the year:'))
if yy%100==0 and yy%4!=0:
    pass
elif yy%4==0:
    DoM[1]=29
else:
    pass
mm,dd,spaces,row=0,1,'   ',1
while mm not in range (1,13):
    mm=eval(input('Enter the month which is legal:'))
total = abs(yy-1900)*365 + abs(yy-1900)%4 + sum (DoM[0:mm-1])+1
column = total%7
print('--------',yy,'.',mm,'--------')
print ('SUN MON TUE WED THU FRI SAT')
print(' '*((4*(column))+1),end='')
for dd in range(1,DoM[mm-1]+1):
    while column==7:
        print()
        column=0
        row+=1
    if dd>(7-column)+1 and dd<=9:
        spaces=' '*2
    elif dd>9:
        spaces=' '
    while row >=2:
        print (' ',end='')
        break
    print (dd,end=spaces)
    column+=1
#使用format和转义能减少代码行数
