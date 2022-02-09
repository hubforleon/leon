# 练习：
#     1）构造一组n*n的阵列，并打印输出
#     2）构造一组数字的范围的阵列，并打印输出
# 目的：
#     1）使用range()函数快速构造一组阵列；
#     2）range()用于定义数字范围的集合
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

    x = range(2,6)
    print("result is :", x)
    for i in x:
        print(i)

Array(3)

# 练习：
#     1）构造键值对，并打印输出；
#     2）构造键值对的集合，并打印输出二维数组；
# 目的：
#     1）了解键值对的定义和使用。
#     2）如何在for循环中遍历使用键值对
def tup():    
    tag, weight = ("apple", 2) #,# ("peal",5),("banana", 6)
    print("tag & weight:",tag, ", ", weight)

    mkt = [("apple", 2),("peal",5),("banana", 6)]
    for i in mkt:
        print(i)
    print("ooooooooooo")
    for k,v in mkt:
        print("k:{}  v:{}".format(k,v))
    print(mkt[0])
    print(mkt[0][0])
    print(mkt[1][0])
    print(mkt[2][0])
    # x = range(mkt)
    # print(x.count)
# tup()

# 练习：
#     1）使用（）来构建数组，并遍历打印；
#     2）使用『』来构建集合，并遍历打印；
#     3）直接用字符串来赋值，并遍历打印；
# 目的：
#     1）构建数组和集合的三种方法。
def fun_set():
    x= ("apple6","orange","peal","banana","tomato")
    print(x)
    for i in x:
        print("this is ",i)
    
    y={5,10,20,30,15,49}
    print("y1=", y)
    for i in y:
        print("this is ",i)
    y=(5,10,20,30,15,49)
    print("y2=", y)
    for i in y:
        print("this is ",i)    

    z= "apple1","orange","peal","banana","tomato"
    print("z='apple1: '",z)
    
    w= ("apple2","orange","peal","banana","tomato")
    print(w)

    # z=set{9,17,18,25,,15}
# fun_set()