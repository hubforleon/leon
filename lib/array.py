def Array(row):
    print("row=", row)
    
    px = ["*" for i in range(row)]
    py = [px for i in range(row)]    
    print(py)

    ux = [["y" for i in range(row)] for i in range(row) ]
    print(ux)

    up = ("apple","orange","juice","banana")
    print(up)
    print("........")
    for i in up:
        print(i)

    x = range(2,4)
    print("result is :", x)

def tup():    
    tag, weight = ("apple", 2) #,# ("peal",5),("banana", 6)
    print("tag & weight:",tag, ", ", weight)

    mkt = [("apple", 2),("peal",5),("banana", 6)]
    for i in mkt:
        print(i)
    print("ooooooooooo")
    print(mkt[0])
    print(mkt[0][0])
    print(mkt[1][0])
    print(mkt[2][0])
    # x = range(mkt)
    # print(x.count)

def fun_set():
    x= ("apple6","orange","peal","banana","tomato")
    print(x)
    for i in x:
        print("this is ",i)
    
    y={5,10,20,30,15,49}
    print(y)

    z= "apple1","orange","peal","banana","tomato"
    print(z)
    
    w= ("apple2","orange","peal","banana","tomato")
    print(w)

    # z=set{9,17,18,25,,15}
#   w=set("hello")