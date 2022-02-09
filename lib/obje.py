class Dog:
    __Numbers = 100

    @property 
    def dog_id(self):
        return self.__dog_id
    def dog_id(self, id):
        self.__dog_id = id
        Dog.__dog_id = id

    
    @property
    def bite(self):
        return self.__bite
    def bite(self, times):
        self.__bite = times
   
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.bite =3
        Dog.__Numbers +=1
        self.dog_id =Dog.__Numbers    
        
    def run(self):
        print("{} is running".format(self.name))
    def speak(self, speak):
        self.bite +=1
        print("{} is speaking, {}, bites {}".format(self.name, speak,self.bite))
        
    @classmethod
    # cls代表无需实例化的方法的类型
    def calculate_bites(cls,times):
        print("cls.bite is ",cls.bite)
        return cls.bite * times

class BlackDog(Dog):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
        # Dog.__Numbers +=1
    def showcolor(self):
        print("dog's name is {}, age is {}, color is {}, id is {}".format(self.name, self.age, self.color, self.dog_id))
        return self.color

        
def showdog_property():
    mydog = Dog("lion",3)
    print("No. dogs. the id is {}".format(mydog.dog_id))
    Hisdog = BlackDog("hua-hua",5,"black")
    print("No.  dogs. the id is {}".format(Hisdog.dog_id))
    sdog = Dog("h-hua",5)
    print("No.  dogs. the id is {}".format(sdog.dog_id))
    Hdog = BlackDog("huhua",5,"red")
    print("No.  dogs. the id is {}".format(Hdog.dog_id))
    Hisdog.showcolor()
    Hdog.showcolor()

    
    # print("mydog.bite is ", mydog.bite)
    # print("hisdog.bite is", Hisdog.bite)
    # mydog.bite =15
    # Hisdog.bite += 1
    # print("mydog.bite is ", mydog.bite)
    # print("hisdog.bite is", Hisdog.bite)

def showdog():
    mydog = Dog("lion",3)
    Hisdog = Dog("hua-hua",5)
    na = str(mydog.name)
    ag = int(mydog.age)

    print("my dog is %s" %na)
    print("it is %d years old" %ag)
    print("my dog is %s. it is %d years old." %(na,ag))
    mydog.run()
    # mydog.speak("miao, miao, miao!")
    # mydog.speak("miao, miao, miao!")
    # mydog.speak("miao, miao, miao!")
    # Hisdog.speak("miao, miao!")
    # print("Dog.bite : Dog bites is {}".format(Dog.bite))   
    # print("mydog bites is {}".format(mydog.bite))
    # print("hisdog bites is {}".format(Hisdog.bite))
    # Dog.bite = Dog.bite +1
    # mydog.bite +=2
    # Hisdog.bite +=5
    # print("Dog.bite : Dog bites is {}".format(Dog.bite))
    # print("mydog.bite +=3 : mydog bites is {}".format(mydog.bite))
    # print("Hisdog.bite +=5: hisdog bites is {}".format(Hisdog.bite))
    
    # print("类方法")
    # x = Dog.calculate_bites(2)
    # print("x= Dog.calculate_bites(2) = {}".format(x))
    # y = mydog.calculate_bites(3)
    # print("x= mydog.calculate_bites(3) = {}".format(y))
    # z = Hisdog.calculate_bites(4)
    # print("x= Hisdog.calculate_bites(4) = {}".format(z))
showdog()
