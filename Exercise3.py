wage = float(input("What is your hourly wage? "))
work = float(input("How many hours do you work? "))
day = input("what is the day today? ").lower()

if day == "sunday":
    print("Hourly wage:", wage*2)
    print("Hours worked:", work)
    print("Day of the week:", day)
    print("Daily wage:", 2 * wage * work)
else:
    print("Hourly wage:", wage)
    print("Hours worked:", work)
    print("Day of the week:", day)
    print("Daily wage:", wage * work)

