import string
space=0
num=0
eng=0
other=0
a=input('Just enter something')
for b in a:
    if b.isalpha():
        eng+=1
    elif b.isspace():
        space+=1
    elif b.isdigit():
        num+=1
    else :
        other+=1
print ('letters:',eng,'numbers:',num,'space:',space,'others:',other)

'''
伪代码如下
declare space
set space = 0
declare num
set num = 0
declare eng
set eng=0
declare other
set other=0
declare string
Write "Just enter something"
input string 
for (b=string[0];b<=string[-1];b++)
    if string[b]==letter
        eng++
    else string[b]==space
        space++
    else string[b]==numbers
        num++
    else :
        other++
Write "letters:"+eng,"numbers:"+num,"space:"+space,"others:"+other

