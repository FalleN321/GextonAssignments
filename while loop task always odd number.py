i=int(input("Enter initial value: "))
l=int(input("Enter limit/ending value: "))
while i<l:
    if i%2 == 0:
        i=i-1
        print(i)
    elif i%2 !=0:
        i=i+2
        print(i)