print("GCS CALCULATOR")

a=input("\nPlease Enter patient's name: ")
print("\nLets start with the eyes:")
e=int(input("""Spontaneously (+4)
To verbal command (+3)
To pain (+2)
No eye opening (+1)       : """ ))

print("\nVerbal response:")
v=int(input("""
Oriented (+5)
Confused (+4)
Inappropriate words (+3)
Incomprehensible sounds (+2)
No verbal response (+1)       : """))

print("Motor response:")
m=int(input("""
Obeys commands (+6)
Localizes pain (+5)
Withdrawal from pain (+4)
Flexion to pain (+3)
Extension to pain (+2)
No motor response (+1)     : """))

GCS=  e+v+m

if GCS == 3:
    print(f"\nNo reponse from {a}")
elif GCS > 3 and GCS <= 6:
    print(f"\n{a} is somewhat responsive")
elif GCS > 6 and GCS <= 10:
    print(f"\n{a} is responsive")
elif GCS > 10 and GCS <= 13:
    print(f"\n{a} is very responsive")
elif GCS > 13 and GCS <= 15:
    print(f"\n{a} is fully responsive")