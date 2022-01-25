def lprint():
    x=278
    y=2792.200
    z="88.123456789"
    a="123456789"
    print("x={0:d}, y={1:s} ".format(x,str(y)))
    print("z={0:e}".format(int(a)))
    print("z={0:e}".format(float(z)))
    print("z={e}".format(float(z)))

def findstr():
    original= "hello world. I am coming."
    result = original.find("or",0,30)
    print("original text is {}. \n the location is {}".format(original, result))

    rep = original.replace("or","OR")
    # print(original)
    # print(rep)

    sp = original.split(" ",2)
    # for item in sp:
    #     print(item)
    # print(sp)    

    # se = set(sp)
    #  se.add("beatiful")
    # se.remove("hello")
    # print(se)

def finddict():
    dict1 = {"a":102,"b":103,"c":102,"d":"red","e":"blue"}
    for kt in dict1:
        print("{} : {}".format(kt,dict1[kt]))
    print(dict1)

    x= dict1.pop("b")
    print("\ndict1.pop(‘b’) is {} ".format(x) )
    print(dict1)

    print("items: {}".format(dict1.items()))
    print("keys: {}".format(dict1.keys()))
    print("list of items: {}".format(list(dict1.items())))
    print(dict1.values())



# findstr()
finddict()
# lprint()


