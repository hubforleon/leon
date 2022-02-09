class Dogs:
    __id=100
    __bites=0

    def __init__(self, uname, uage):
        self.name = uname
        self.age = uage
        Dogs.__id +=1
        self.__bites = 0

    @property
    def id(self):
        return self.__id

    def id(self, newid):
        self.__id = newid

    def run(self):
        print("%s is running! it is %d years old. ID:%d" %(self.name, self.age, self.__id))

    def bite(self):
        self.__bites +=1
        Dogs.__bites +=1
        s="Wan "*self.__bites
        p=["--- " for i in range(self.__bites)]
        print("%s bites %d. %s" %(self.name, self.__bites,s))
        # print("%s bites %d. %s" %(self.name, self.__bites,p))

    @classmethod
    def stat(cls):
        print("dogs has bites %d times. " %(cls.__bites))

class BlackDogs(Dogs):
    'this is blackdog from Dogs class'
    def __init__(self, uname, uage, ucolor):
        Dogs.__init__(self,uname, uage)
        self.color = ucolor

    def show(self):
        print("%s color is %s" %(self.name, self.color))

dog1=Dogs("k1",18)
dog1.bite()
dog1.run()
dog2=BlackDogs("k2",20,'black')
dog2.bite()
dog2.bite()
dog2.run()
dog2.show()
dog3=Dogs("k3",20)
dog3.bite()
dog3.bite()
dog3.run()
print("--"*10)
dog4=BlackDogs("k4",20,'black')
dog1.bite()
dog4.bite()
dog4.bite()
dog4.run()
dog4.show()
print("**"*10)
dog5=Dogs("k5",20)
dog1.bite()
dog2.bite()
dog3.bite()
dog5.bite()
dog5.bite()
dog5.bite()
dog5.run()
dog5.stat()
dog2.stat()
