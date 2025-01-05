
class Time:
    def __init__(self,h,m,s):
        self.hour=h
        self.min=m
        self.sec=s
    def display(self):
        print("Hour:Minute:Second")
        print(f"{self.hour}:{self.min}:{self.sec}")
    def __add__(self,other):
        h=self.hour+other.hour
        m=self.min+other.min
        s=self.sec+other.sec

        if s>=60:
            m+=int(s/60)
            s=s%60
        elif m>=60:
            h+=int(m/60)
            m=m%60
        t3=Time(h,m,s)
        return t3

t1=Time(3,45,56)
t2=Time(4,50,40)
t3=t1+t2
t3.display()