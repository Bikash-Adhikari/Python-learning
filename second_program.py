x = int(input("Enter number first:"))
y = int(input("Enter number second:"))
z = int(input("Enter number third:"))

if(x > y and x > z):
    gratestnum = x

elif (y > z):
    gratestnum = y

else:
    gratestnum = z


print("Gratest number among ", x ,",", y, ",",z, "is", gratestnum)