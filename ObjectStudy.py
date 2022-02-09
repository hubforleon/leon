class Dogs:
    __id =100
    __bite = 0
    __total_bite = 0

    def __init__(self, uname, uage):
        self.name = uname
        self.age = uage
        # self.sex = usex
        Dogs.__id +=1
        self.id = Dogs.__id
        self.__bite =0
    
    @property
    def __Dog_id(self):
        return self.__id

    def __Dog_id(self,id ):
        self.__id = id
        Dogs.__id = id+1

    def run(self):
        print("{} is running".format(self.name))

    def bite(self):
        self.__bite +=1        
        Dogs.__bite +=1
        Dogs.__total_bite +=1
        print("{} --ID:{}: Wang Wang Wang. it has bited {} times.".format(self.name, self.id, self.__bite))

    @classmethod

    def stat(cls):
        print("Total bites {} times. Dogs.__bite is {}.".format(cls.__total_bite, Dogs.__total_bite))
    
class BlackDogs(Dogs):   
    def __init__(self, uname, uage, ucolor):
        super().__init__(uname, uage)
        self.color = ucolor

    # @property
    def show(self):
        print("{} is a blackDog.  Its color is {}".format(self.name, self.color))

dog1 = Dogs(uname="k1", uage=18)
dog2 = Dogs("k2", 20)
dog3 = BlackDogs(uname="HHH", uage=18, ucolor="black")
dog1.run()
dog1.bite()
dog2.bite()
dog2.bite()
dog2.bite()
dog3.bite()
dog3.bite()
dog1.bite()
dog1.bite()
dog3.bite()
dog3.bite()
dog2.bite()
dog2.bite()


# dog3.bite()
# dog3.show()
# dog1.stat()
# dog2.stat()
# dog3.stat()

def single():
    for num in range(10,20):
        for i in range (2,num):
            if (num%i==0):
                j=num/i
                print("%d 等于 %d * %d" %(num, i, j))
                break
        else:
            print("{} 是质数".format(num))
single()



