cabtype = ["uberx", "uberxl", "uberplus", "uberblack", "ubersuv"]
fare = [3, 5, 7, 10, 13]
length = 31

for i in range(4, -1, -1):
    if length * fare[i] <= 200:
        print(cabtype[i])
        break