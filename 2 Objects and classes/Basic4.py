class Book(object):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_details(self):
        print("The book i am reading is called a", self.title, "and the writer is known as", self.author, "and the price is" , self.price)
        #print(self.title, self.author, self.price)
    def update_price(self, new_price):
        self.price = new_price
        
        
books1 = Book("Bible", "God", 2000)
books1.display_details()
books2 = Book("Hymm Book", "Jesus", 1000)
books2.display_details()
books1.update_price(5000)
books1.display_details()
books2.display_details()