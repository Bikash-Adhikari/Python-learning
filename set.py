# empty set
collection = set()
print(collection)
print(type(collection))


#Set Functions ================================================
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






