def compare(a,b):
    print("a= ", a, "  b= ",b)
    print("a > b:  ",a>b)
    print("a < b:  ",a<b)
    print("a != b:  ",a!=b)
    print("a == b:  ",a==b)
    print("a >= b:  ",a>=b)
    print("a <= b:  ",a<=b)
    
def logy_op(x1,x2,x3,x4):
    a= x1>x2
    b = x3>x4
    print("a= x1>x2 = ",a,"  b= x3>x4 = ",b)
    print("a and b :", a and b)
    print("a or b :", a or b)   
    print("not a:", not a)
    print("not b:", not b)

def criteria(num):
    if num > 10:
        return True
    else:
        return False

def filtred(numbers):
    x = filter(criteria, numbers)
    y = list(x)
    return y

def selfadd(num):
    num+=5
    return num

def mapping(numbers):
    x = map(selfadd,numbers)
    return list(x)
