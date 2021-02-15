# task 1 : design an online banking system , that have only 3 options
# >> deposit
# >> withdraw
# >> display
# >> exit
banking = True
amount = 12500
print("Welcome to online banking")


while banking=True:
    i = int(input(""">> deposit(1)
    >> withdraw(2)
    >> display(3)
    >> exit(4)
    """))

    if i == 1:
        d = int(input("How much amount would you like to deposit?: "))
        amount = amount + d
        print(f"your new balance is ", amount)




    elif i == 2:
        w = int(input("Enter the amount you would like to withdraw: "))
        if w <= amount:
            n = []
            amount = amount - w
            n.append(w)
            print("you withdraw", w, "\nyour new balance is", amount)
        else:
            print("Sorry not enough cash")

    elif i == 3:
        print(f"Your current amount is {amount}")


    elif i == 4:
        print("Thankyou for online banking!")
        banking=False
