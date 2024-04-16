#==========================================================================================
# For in Loops
#===>> loops are used for sequential traversal. For traversing LIST, STRING, TUPLES etc
#===>> Sequential traversal means==> travel index wise gradually in the list, string, tuple etc


#==========for in loop================================================
list = [3, "Bikash", 400, "life"]

for i in list:
    print(i)



# ================ for in loop with else ==============================
tup = (2, 4, 6, 8, 10)

for el in tup:
    print(el)

else:
    print("For in else loop End")    



#====PRactice============================================================ find 8 
nums = [1,2,3,4,5,6,7,8,9,99,8]

x = 8
i = 0
for el in nums:
    if(el == x):
        print("the number 8 is found at index", i)
    i +=1    