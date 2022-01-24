def star(star_count):
    i = 1
    print("Function star execution:")


    while i <= star_count:
        print("*"*i)
        i += 1
    else:
        print("it is done!")
        print("start_count =",star_count, " i=",i)

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






    