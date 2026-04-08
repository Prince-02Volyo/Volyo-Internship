inpstring = input("Enter the String: ")

mid = len(inpstring) // 2 

if len(inpstring) % 2 != 0:
  print("False") 

else :
  inpstring[:mid]==inpstring[mid:]
  print("true")

