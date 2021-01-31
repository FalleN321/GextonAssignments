toyota = ["Corolla","Aqua","Yaris"]
honda = ["Civic","City","CRZ"]
suzuki = ["Alto","Swift","Cultus"]

print("=============HELLO AND WELCOME=================")

brand = input("Please Tell us the brand of the car : ").capitalize()
if brand == "Toyota":
    print(f"These are the available Cars: \n{toyota}")
elif brand == "Honda":
    print(f"These are the available Cars: \n{honda}")
elif brand == "Suzuki":
    print(f"These are the available Cars: \n{suzuki}")
else:
    print("Sorry The brand does not exist")

module = input("Which one would you like to buy? : ").capitalize()

if brand == "Toyota" and module == "Corolla":
    i = input("its price is 2.5 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Toyota" and module == "Aqua":
    i = input("its price is 2.1 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Toyota" and module == "Yaris":
    i = input("its price is 2.9 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Honda" and module == "Civic":
    i = input("its price is 4.5 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Honda" and module == "City":
    i = input("its price is 2.4 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Honda" and module == "Crz":
    i = input("its price is 1.8 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Suzuki" and module == "Alto":
    i = input("its price is 1.5 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Suzuki" and module == "Swift":
    i = input("its price is 2.2 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")
elif brand == "Suzuki" and module == "Cultus":
    i = input("its price is 2.0 million , Would you like to buy? yes (1) or no (0): ")
    if i == "1":
        print("Thankyou for your Purchase.")
    else:
        print("Okay , Come again!")

