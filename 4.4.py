a=input("Enter a string:")
for i in range(len(a)):
    if a[i]==a[-(1+i)]:
        if i==(len(a)//2)+1:
            print('YES!')
            break
        else:
            continue
    else:
        print('No')
        break
