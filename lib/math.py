from email import charset


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


def tri(row):
    i=0
    pics = [0 for i in range(row)]

    while (i<row):
        j=0
        while(j<2*row):
            # pics[i][j]= har(" ")
            j+=1
        i +=1
    while (i<row):
        j=0
        while(j<2*row):
            if (j>=(row-i) and (j<(2*row -i))):
                pics[i][j] = "*"
                j+=1
            i+=1
    print(pics)


def digital():
    x = 100
    print("x=",x, "...",type(x))

    x=True
    print("x=",x, "....",type(x))

    x=5+6j
    print("x=",x, "....",type(x))
    y=3+2j
    print("x+y=",x+y, "....",type(x+y))

    x=5
    y = float(x)+1.0
    print("x=",x, "....",type(x), "y = float(x)+1.0=",y, "....",type(y))

    x=17
    y=5
    print("x=",x," y=",y)
    print("x+y= ",x+y)
    print("x-y= ",x-y)
    print("x*y= ", x*y)
    print("x/6= ", x/y)
    print("x%y= ", x%y)
    print("x//y= ",x//y)

    x=5
    y=2
    print("\n x=",x," y=",y)
    print("x**y=",x**y)

def di_op(x,y):
    print("x =",x, " y =",y)
    a = x
    b=y
    a+=b
    print("x += y :", a)
    a=x
    a-=b
    print("x -= y :", a)
    a=x
    a*=b
    print("x *= y :", a)
    a=x
    a/=b
    print("x /= y :", a)
    a=x
    a%=b
    print("x %= y :", a)
    a=x
    a//=b
    print("x //= y :", a)
   
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def cal(operator):
    if operator == "+":
        return add
    else:
        return sub

f1 = cal("+")
f2 = cal("-")

def calc(operator):
    if operator =="+":
        return lambda a,b : (a+b)
    else :
        return lambda a,b: (a-b)



    