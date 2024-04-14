
#=======BREAK==========================================
idx = 0
while idx <= 10:
    print(idx)
    if(idx == 3):
        break    # it stops the execution of iteration of the code after print the value at 3rd index
    idx += 1


#=============CONTINUE====================================

i = 0
while i <= 10:
    if(i == 5):
        i += 1
        continue
    print(i)
    i += 1