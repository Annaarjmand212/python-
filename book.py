class Book:
    def __init__(self , title , author , year ):
        self.title= title
        self.author= author
        self.year= year
        self.is_borrowed= False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed= True
            print("Book is borrowed successfully .")
        else:
            print("Book is already borrowed")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("Book returned successfully.")
        else:
            print("Book is already available")
    def show_info(self):
        print(f"Book title: {self.title}")
        print(f"Book author: {self.author}")
        print(f"Book made year: {self.year}")
        if self.is_borrowed == True:
            print("Status : Unavailable")
        else:
            print("Status : Available")
