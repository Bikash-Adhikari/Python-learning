
# def myFunction(x, y):
#     sum = x + y
#     return sum


# s = myFunction(5, 9)
# y = myFunction(3, 9)
# print("the sum is", s, "and", y)




#  (1) WAF to print the length of a list. (list is the parameter)

list = ["Grapes", "Banana", "Papaya", "Watermelon", "Apple", "Pineapple","Orange"]
uni = {"Stanton", "UTtyler, Murray", "Webster", "Standford", "Manipal"}
num = (3, 5, 66, 89, 90, 334, 7867, 55,9000,170000)

#function to print length---------------------------------------------
def func(para):
    L = len(para)
    print(L)
    return L

func(list)
func(uni)
func(num)

#function to print all values in single line-------------------------------
def Fun_val(para):
    x = para
    print(x)
    return x

Fun_val(list)
Fun_val(uni)
Fun_val(num)
