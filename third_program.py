a = int(input("Enter a number as you like:"))

R = a % 7 

if(R == 0):
    result = " is multiple of 7."
else:
    result = " is not multiple of 7"


print("The number you entered ", a, result)