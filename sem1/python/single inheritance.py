class A:
    def __init__(self):
        print("In A")
    def f1(self):
        print("f1 in A")
class B(A):
    def __init__(self):
        super().__init__()
        print("In B")
    def f1(self):
        super().f1()
        print("f1 in B")

obj=B()
obj.f1()