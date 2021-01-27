
# #Calculator

a=int(input("Enter your first number: "))
b=input("Enter the operator: ")
c=int(input("Enter your second number: "))

if b == "+":
    print("\n" +str(a+c))
elif b == "-":
    print("\n" +str(a-c))
elif b == "/":
    print("\n" +str(a/c))
elif b == "*":
    print("\n" +str(a*c))
elif b == "&":
    print("\n" +str(a&c))
elif b == "|":
    print("\n" +str(a|c))
elif b == "<":
    print("\n" +str(a<c))
elif b == ">":
    print("\n" +str(a>c))
elif b == "<=":
    print("\n" +str(a<=c))
elif b == ">=":
    print("\n" +str(a>=c))

