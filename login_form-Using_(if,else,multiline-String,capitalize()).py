name=input("Enter your name: ").upper()
password = int(input("Enter your password: "))
email = input("Enter your Email: ").lower()

if name == "AHAD" and password == 123 and email == "ahad470@gmail.com":
    print(f"""You've been recognized! 
Welcome! {name}""")
elif name == "Hanzillah" and password == 456 and email == "hanzillahabro@gmail.com":
    print(f"""You've been recognized! 
Welcome! {name}""")
elif name == "Tahir" and password == 789 and email == "tahirrazzaq@gmail.com":
    print(f"""You've been recognized! 
Welcome! {name}""")

else:
    print("Sorry you're not recognized!")
