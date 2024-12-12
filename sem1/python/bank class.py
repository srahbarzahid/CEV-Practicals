class Bank:
    def __init__(self,ac_no,name,type,bal):
        self.ac_no=ac_no
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amt):
        if amt<=0:
            print("amount should be positive")
            return
        else:
            self.bal+=amt
            print(f"current balance is {self.bal}")
    def withdraw(self,amt):
        if self.bal<=0:
            print("your balance is zero")
            return
        elif amt>self.bal:
            print("insufficient balance")
            return
        elif amt<=0:
            print("amount must be positive")
            return
        else:
            self.bal-=amt
            print(f"yor current balance is {self.bal}")
    def display(self):
        print(f"Account Number: {self.ac_no}")
        print(f"Account holder: {self.name}")
        print(f"Account type: {self.type}")
        print(f"Yor current balance: {self.bal}")


name=input("enter a name: ")
ac_no=int(input("enter the account number: "))
type=input("enter the account type: ")
bal=int(input("enter the balance: "))

account= Bank(ac_no,name,type,bal)

while True:
    print("\n1)DEPOSIT\n2)WITHDRAWAL\n3)ACCOUNT INFORMATION\n4)EXIT\n")
    ch=int(input("enter your choice"))

    if ch==1:
        amt=int(input("enter your amount: "))
        account.deposit(amt)
    elif ch==2:
        amt=int(input("enter yor withdrawal amount: "))
        account.withdraw(amt)
    elif ch==3:
        account.display()
    elif ch==4:
        print("-----exited-----")
        exit(0)
    else:
        print("invalid choice")