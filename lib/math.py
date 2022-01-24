def star():
    x = 1
    y = 5
    i = x
    print("Function star execution:")


    while i <= y:
        print("*"*i)
        i += 1
    else:
        print("it is done!")
        print("x=",x," y=",y, " i=",i)

def triangle(row):
    print("Function triangle begins:")
    if (row <=0):
        print("input error, row and column must be above 0!")
        return False
    elif row >10:
        print("imput number is too large.")
        return False
    else:
        count = 1
        while count<=row:
            print(" "*(row-count)," *"*count)
            count +=1
           # print("i=",count) 
            
    return True






    