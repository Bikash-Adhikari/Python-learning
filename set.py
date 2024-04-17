# empty set
collection = set()
print(collection)
print(type(collection))


#Set ====================================================
x = {1, 3, 3, 5, 7, 9, 9, 11, 13.3}
y = {"Ram", "Sita", 1, 5, 13.3}

print(x) 
print(y)

x.add("Bikash")  #=========== add an element
print(x)

y.remove("Sita") #============remove an element
print(y)

x.clear() #=================== To make the set empty
print(x)


y.pop() #======================= remove the random value from set
print(y)

print(len(x)) #==================length of set

#=================================================================
#=================================================================
#--------------------Union and Intersection-----------------------

A = {1, 2, 3}
B = {3, 4, 5}

C = A.union(B) #----------------Set Union
print(C)

D = A.intersection(B) #---------------Set Intersection
print(D)

#=========================================================================
'''-------SOME IMPORTANT NOTES ON SET-------'''
#=========================================================================

# Set is the collection of unordered items.
# Each element in the set must be unique and immutable
# We can store the following value in set
    #---integer
    #---float
    #---string
    #---tuple
    #---boolean

# BUT= List and Dictionaries can not be used since they are "MUTABLE"    
# set has stored its value only inside the {} curly braces.
# Duplicate values are ignored by set. If we store same value, set will execute only one value every time
# print(lent(set))=== will print only the count of distinct value.
# set assume and tread 9 and 9.0 as the same data type.

# set is mutable [since it can be changed]
# but elements in set are immutable [since they cant be changed]

# in set union and intersection == it method returns the new set and dont change the old one






