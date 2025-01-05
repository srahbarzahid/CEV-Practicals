class Bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amt):
        if amt<0:
            print("amount should be positive")
        else:
            self.bal+=amt
    def withdraw(self,amt):
        if amt>self.bal:
            print("insufficient balance")
        elif amt<0:
            print("it should be positive")
        else:
            self.bal-=amt
    def display(self):
        print(f"Account No:{self.accno}")
        print(f"Name:{self.name}")
        print(f"Type:{self.type}")
        print(f"Balance:{self.bal}")

user1=Bank(23344,"amal","savings",3400)
while True:
    print("1.Deposit\n2.Withdraw\n3.Display\n4.Exit\n")
    opt=int(input("enter the option:"))
    if opt==1:
        amt=int(input("enter the amount: "))
        user1.deposit(amt)
    elif opt==2:
        amt = int(input("enter the amount: "))
        user1.withdraw(amt)
    elif opt==3:
        user1.display()
    elif opt==4:
        exit(0)
    else:
        print("invalid option")