a1=eval(input('Enter the first number'))
a2=eval(input('Enter the second number'))
a3=eval(input('Enter the third number'))
a4=eval(input('Enter the fourth number'))
a5=eval(input('Enter the fifth number'))
print ('The sum is:',a1+a2+a3+a4+a5)

#Improved version as follow:
print(Another verison:)
time = 11
list=[]
SUM=0
while time>=10 or time<=0:
    time=eval(input("Enter how many times you want to plus"))
for i in range(1,time+1):
    num=eval(input('Enter the number'))
    list.append(num)
    i+=1
for j in list:
    SUM+=j
print ('The result:',SUM)

'''
伪代码如下
Write "Enter 5 numbers"
Input a1
Input a2
Input a3
Input a4
Input a5
set average =(a1+a2+a3+a4+a5)/5
Write "The average is:"+average
-----------Better one------------
declare time
set time = 11
declare list = [] 
declare SUM 
set SUM =0
declare num
while time>=10 or time<=0 then
    Write "Enter how many times you want to plus"
    Input time
for (i=1;i<=time;i++):
    Write "Enter the number"
    Input list[i]
    i++
for (j=1;j<=time;j++)
    SUM=SUM+list[j]
Write "The result:"+SUM
'''
