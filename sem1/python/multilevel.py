class Publisher:
    def __init__(self,name):
        self.name=name
        print("\n1st class activated")
    def display(self):
        print(f"publisher: {self.name}")
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        print("2nd class activated")
        self.name=name
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
class Python(Book):
    def __init__(self,name,title,author,price,no):
        super().__init__(name,title,author)
        print("3rd class activated\n")
        self.name=name
        self.title=title
        self.author=author
        self.price=price
        self.no=no
    def display(self):
        super().display()
        print(f"Price: {self.price}")
        print(f"Number of pages: {self.no}")

book1=Python("DC","aadujeevitham","Basheer",1650,250)
book1.display()