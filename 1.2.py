mon=-1
while mon<0:
    mon=eval(input('Enter the money more than 0:'))
if mon<=50000:
    tax=mon*0.05
elif mon<=100000:
    tax=2500+(mon-50000)*0.07
elif mon>100000:
    tax=6000+(mon-100000)*0.09
print ('The tax are:',tax)

'''
declare mon=-1
while mon<0 then
    Write "Enter the money more than 0:"
    input mon
if mon<=50000 then
    tax=mon*0.05
else mon<=100000 then
    tax=2500+(mon-50000)*0.07
else mon>100000 then
    tax=6000+(mon-100000)*0.09
End if
Write "The tax are:"+tax
'''