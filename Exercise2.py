name = input("Please tell me your name ").lower()

if name == "matti":
    print("Next please!")
else:
    portions = int(input("How many portions of Soup? "))
    print(portions*5.90)
