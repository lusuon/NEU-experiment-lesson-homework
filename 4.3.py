n,MA,MB,MC,MCr,SUM,count,COUNT,C=0,[],[],[],[],0,0,0,0
while n<=0:
    n=eval(input("Enter  matrixs' rows and columns,should be postive:"))
print("Matrix A")
for i in range(n):
    row = input("Enter numbers less than Maxtix's column,use space to seperate:")
    while len(row.split())!=n:
        row = input("Enter numbers less than Maxtix's column,use space to seperate:")
    MA.append(tuple(eval(j) for j in row.split()))
print("Matrix B")
for i in range(n):
    row = input("Enter numbers less than Maxtix's column,use space to seperate:")
    while len(row.split())!=n:
        row = input("Enter numbers less than Maxtix's column,use space to seperate:")
    MB.append(tuple(eval(j) for j in row.split()))
for COUNT in range(n):
    while C<=n-1:
        for count in range(n):
            SUM+=MA[COUNT][count]*MB[count][C]
        MCr.append(SUM)
        SUM=0
        C+=1
        if len(MCr)==n:
            MC.append(tuple(MCr))
            MCr,SUM=[],0
    C=0        
for j in MC:
    print(j)



