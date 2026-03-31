a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Highest number is:", a)
elif b >= a and b >= c:
    print("Highest number is:", b)
else:
    print("Highest number is:", c)