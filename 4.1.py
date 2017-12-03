count,passer,great,fail=1,0,0,0
scores=[]
while count<=30:
    scores.append(eval(input("Enter the student's score:")))
    count+=1
for i in scores:
    if i>=60 and i<90:
        passer+=1
    elif i>=90:
        great+=1
    else:
        fail+=1
print("Passer(60~90):",passer,"Great guys(>=90):",passer+great,"Loser:",fail)

'''
count,passer,great,fail=1,0,0,0
scores=[]
while count<=30 then
    scores.append(eval(input("Enter the student's score:")))
    count++
for i in scores :
    if i>=60 and i<90 then
        passer++
    else i>=90 then
        great++
    else 
        fail++
Write "Passer(60~90):"+passer+"Great guys(>=90):"+passer+great+"Loser:"+fail

'''
