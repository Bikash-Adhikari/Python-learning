#Practice:  Check if list contains a palindrome of elements.

list1 = [1, 2, 1]
list2 = [1, 2, 3]


#for list 1
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("list1 has palindrome elements.")
else:
    print(" List1 has Not Palindrome")    

#for list 2
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("List2 has palindrome elements.")
else:
    print("List2 has NOT palindrome elements.")    



