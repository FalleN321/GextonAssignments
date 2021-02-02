#1 ) Ask user to enter his email that should have .com in the end

e = input("Enter your email: ").endswith(".com")

if e == True:
    print("Thankyou!")
else:
    print("wrong")

#=====================================================================

#2)                  Hello! ( user name ) .. should be titled

username = input("Your username: ").title()
print(f"Hello! {username}".center(50))

h=input("I hope you're fine, How can I help you?: ")

if h =='yes' or h=='yes,please':
    print(f"Sure! {username} we will resolve your problem".center(50))
else:
    print(f"Good to see you {username} , stay connected")



#================================================================
#isalnum TASK
p=input("Enter your password with alphabets and numbers: ").isalnum()
print(p)


#================================================================

#URL task

u=str(input("Enter your URL: "))

if u.startswith("http://www."):
    i=input("What would you like to end it with?:")
    if i.endswith((".com",".net")):
        pass
    print(u+i)