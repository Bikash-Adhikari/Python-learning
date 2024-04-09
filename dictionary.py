# define a dictionary
dict = {
    "name" : "Bikash Adhikari",
    "CGPA" : 3.5,
    "marks" : [98, 86, 89, 87]
}

# access the value of dictionary

y = dict["CGPA"]
print(y)

print(dict["marks"])

#=======================================================
# to add new "key" and "value to the above dict"
dict["age"] = 34
dict["University"] = "Murray Stage University"
dict["Country"] = "USA"

print(dict)

#=========================================================
#work with nested dictionary==============================
student = {
    "name" : "Bikram Adhikari",
    "subject" : {
        "math" : 98,
        "science" : 88,
        "computer" : 99
    },
    "faculty": "Computer Science"
}

# work with Dictionary Methods
keys = student.keys()
print(keys)
print(list(student.keys())) #=============typecasting=====Dict to list and print

x = student.values() #=================to print all value of the Dictionary
print(x)

y = student.items() #===============return tuple of key value inside the list
print(y) 

z = student.get("name")
print(z)

print(student.get("subject"))

m = student["subject"] ["computer"]  #========prints nested dictionary value
print(m) 

student["Home Country"] = "Nepal" #=======added new key:value to the dict
print(student)


print(list(student.keys()))   #=============typecasting=====Dict to list and print






