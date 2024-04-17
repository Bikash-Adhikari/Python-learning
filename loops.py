#loops are used to repeat the instructions
#-----While Loop----

# count = 1
# while count <= 5 :
#     print("Using while loop")
#     count += 1

# print(count)

i = 1
while i <= 5:
    print("hello", i)
    i += 1

print(i)


j = 5
while j >= 1 :
    print("Hello", j)
    j -= 1

print(j)


#print the multiple of "any num"
n = int(input("Enter a num and create mul table:"))
idx = 1
while idx <= 10:
    print(n," x ",idx ," = ", n*idx)
    idx +=1


#==========---Practice----=================================
# print the following element of list using "While Loop"
# [1, 4, 9,16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9,16, 25, 36, 49, 64, 81, 100]

index = 0
while index < len(list) :
    print(list[index])
    index += 1