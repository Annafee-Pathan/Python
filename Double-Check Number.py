num=int(input("Give a number:"))
if num>50:
    print("Your number is greater than 50.")
    if num%2==0:
       print("And it is even.")
    else:
       print("And it is odd.")
else:
    print("Your number is less than 50.")