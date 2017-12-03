import random
win,time=0,0
Random=random.randint(1,100)
minus,maxium,wrong,Try=1,100,0,'Y'
while Try=='Y'or Try=='y':
    b=eval(input('Guess a number'))
    print(Random)
    if b==Random:
        print ('Congratulations,the number is:',Random)
        win+=1
        wrong=0
        Random=random.randint(1,100)
        time+=1
        Try=input('You win,wanna play again?(Y)or give up(Any key not Y)')
    elif b<Random:
        minus=b
        wrong+=1
        print('The range is:[',minus,maxium,']')
    elif b>Random:
        maxium=b
        wrong+=1
        print('The range is:[',minus,maxium,']')
    if wrong ==3:
        wrong = 0
        time+=1
        Try=input(('You have wrong 3 times and the right answer is:',Random,'Try again?(Y) or give up(Press any key not Y))'))
        Random=random.randint(1,100)
print ('The random number produce',time,'times','You have win',win,'times')
