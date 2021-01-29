#=========================================
           #TASK 1
#=========================================

w = int(input("Enter your weight in Kg: "))
print("perfect! now lets measure your height. \n")
m = input("What would you like your height to be measured in? (Meter,inches or foot):   ").lower()
print("Great!")
if m == "inches":
    i = float(input("what is your height in inches?: "))
    h = i/39.37
elif m == "foot":
    f = float(input("What is your height in foot?: "))
    h = f/3.281
elif m == "meter":
    meter = float(input("what is your height in meters?: "))
    h = meter
else:
    print("Please provide a valid input")

kg = w
h2 = h*2
BMI = kg/h2
print(float(BMI))

if BMI < 18.5:
    print("sorry you're too under weight for this job.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are perfect for this job")
elif BMI > 25 and  BMI <= 29.9:
    print("You are too over weight for this job.")
elif BMI >= 30:
    print("Obesity")

#=================================================
               #TASK 2
#=================================================
print("\n")
print("Now Lets fill out the form so we can see if you're eligible")

print("=========== WELCOME ==============")
print("Please Fill out the follwing: ")
name = input("Name: ").capitalize()
print("...........................")
qualification = input("Qualification: ").lower()
print("...........................")
age = int(input("Age: "))
print("...........................")
gender = (input("Gender: ")).capitalize()
print("==============X==============")

if qualification == "graduated" and gender == "Male" and age > 20 and age < 35 :
    print(f"{name} You are applicable to apply!")
elif qualification == "intermediate":
    print("sorry")
elif qualification == "masters" and gender == "Male" and age > 20 and age < 35 :
    print("{} you are applicable to apply ".format(name))
elif qualification == "graduated" and gender == "Female" and age > 20 and age < 35 :
    print("Sorry we're looking for male assistance "+ name)
else:
    print("you're not eligible")