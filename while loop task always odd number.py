i=int(input("Enter the initial state: "))
a=int(input("Enter the final state: "))

while i<a:


    if i%2==0:
        i=i+1
        print(i)

    elif i%2!=0:
        print(i)

    i=i+1
