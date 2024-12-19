class Main:
    def __init__(self,name):
        self.name=name
        print("activate main class")
    def f1(self):
        print(self.name)
class Main1:
    def __init__(self,age):
        print("main2 function is activate")
        self.age=age
    def f1(self):
        print(self.age)
class sub(Main,Main1):
    def __init__(self,name,age):
        super().__init__(name)
        Main1.__init__(self,age)
    def f1(self):
        super().f1()
        Main1.f1(self)

obj=sub("rahbar",21)
obj.f1()
