def check_eligibility():
    gender = input("Enter your gender (male/female): ")
    age = int(input("Enter your age: "))

    if gender == "male" or "m":
        if age >= 21:
            print("You are eligible for marriage")
        else:
            print("You are not eligible for marriage")
    
    elif gender == "female" or "f":
        if age >= 18:
            print("You are eligible for marriage")
        else:
            print("You are not eligible for marriage")
    
    else:
        print("Invalid gender entered")

check_eligibility()