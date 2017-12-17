DoM = [31,28,31,30,31,30,31,31,30,31,30,31]
yy=eval(input('Enter the year:'))
def leap():
    if (yy%100!=0 and yy%4==0) or yy%400==0:
       global DoM
       DoM[1]=29
       
def S_print(dd):
    if dd<10:
        print('',dd,' ',end='')
    else:
        print(dd,' ',end='')
def PRINT(mm):
    global DoM,yy
    total = abs(yy-1900)*365 + abs(yy-1900)%4 + sum (DoM[0:mm-1])+1
    column = total%7
    print()
    print('--------',yy,'.',mm,'--------')
    print ('SUN MON TUE WED THU FRI SAT')
    print(' '*(column*4),end='')
    for dd in range(1,DoM[mm-1]+1):
        S_print(dd)
        column+=1
        if column==7:
            print()
            column=0           
def main():
    leap()
    for i in range(1,13):
        PRINT(i)
main()
