classes =eval(input('Enter the number of classes'))
sumscore = 0
stu,i=0,0
for i in range(classes):
    print('Now:class',i+1)
    stunum =eval(input('Enter the students number in the class'))
    while stunum>50:
        stunum=eval(input('Error,please enter the number less than 50:'))
    while stu<stunum:
        score=eval(input('Enter the score:'))
        sumscore=sumscore+score
        stu+=1
    print('class',i+1,''' 's Total score:''',sumscore)
    stu=0
    sumscore = 0

'''
declare classes 
Write "Enter the number of classes"
Input classes
declare sumscore
set sumscore = 0
declare stu = 0
set stu=0
declare i
set i =0
for (i=1;i<=classes;i++)
    Write "Now:class"+(i+1)
    decalre stunum
    Write"Enter the students number in the class"
    input stunum
    while stunum>50 then
        Write "Error,please enter the number less than 50:"
        input stunum
    while stu<stunum then
        Write "Enter the score"
        input score
        sumscore=sumscore+score
        stu++
    Write "class"+i+1,":sumscore"
    stu=0
    sumscore = 0
'''
