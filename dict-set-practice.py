# Store the folloing word meaning in python dictionary
# table : "a piece of furniture" , "list of facts and figure"
# cat : "a small animal"

mean = {
    "table" : ("a piece of furniture", "list of facts and figure"),
    "cat" : " a small animal"
}

print(mean)
print(mean.keys())
print(mean["cat"])
print(mean["table"])


# set to find the no of classroom for different subjects
classRoom =  {
    "Python", "JAVA", "C++", "Python", "Javascript", "JAVA", "Python", "C++", "C#"

}
x = len(classRoom)
print("No of class required =", x) # not of class required


# Dictionary====input====store marks of diff subj in dict

marks = {}
sciencem = int(input("Marks on Science:"))
mathsm = int(input("Marks on Mathematics:"))
socialm = int(input("Marks on Scoial Studies:"))

#====Method1
# marks["science"] = sciencem
# marks["Mathematics"] = mathsm
# marks["Social Studies"] = socialm

#====Method2
marks.update({"Science" : sciencem})
marks.update({"MathMatics" : mathsm})
marks.update({"Social Studies" : socialm})


print(marks)
print(type(marks))




