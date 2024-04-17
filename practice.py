#  (1).. print the element of the following list using a loop

# myList = [1, 7, 34, 56, 26, 88, 90, 65, 32, 66, 99]
# i = 0

# for el  in myList:
#     print("element in the list", "at the index", i, "is", el)
#     i += 1



#  (2)..Search for a number in this tupple 

# myTup = (1, 7, 34, 56, 26, 88, 90, 65, 32, 66, 99,88)

# x = 88
# i = 0
# for el in myTup:

#     if(el == x):
#         print("The number",x, "is found at the index", i)
#     i += 1


#  (3)..Print numbers from 1 to 100 using range() and for-in loop
# x = range(1,101, 1)
# for el in x:
#     print(el)


# (4).. Print numbers from 100 to 1 using range() and for-in loop      
# for el in range(100, 0, -1):
#     print(el)


# (5).. print the multiplication table of number n using input, range() and for-in loop
# y = int(input("enter a numner 1 to 100 :"))
# z = range(1, 11, 1)

# for el in z:
#     m = el * y
#     print("The multiply of ", y, "x", el, "is", m)


# (6)..WAP to find the sum of first n number. (using while loop)

# x = int(input("Enter a numner: "))

# i = 0
# sum = 0
# while i <= x:
#     sum = sum + i
#     i += 1

# print("The sum of first ",x,"numbers is", sum)    


# (7).. WAP to find the factorial of first n numbers (using for-in loop with range())
# x = int(input("Enter a number:"))

# y = range(1, x+1, 1)
# factoMul = 1
# for el in y:
#     factoMul = factoMul * el

# print(factoMul)


# (8).. WAP to find the factorial of first n numbers (using while loop)

x = int(input("Enter a numner: "))
i = 1
facto = 1
while i <= x:
    facto *= i
    i += 1

print("factorial of ",x, "=", facto)



