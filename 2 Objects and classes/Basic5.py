class Movie(object):
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        
    def display_info(self):
        print("The movie i am watching is called", self.title, ", the director is known as", self.director, ", was made in the year", self.year, "and has a rating of", self.rating)
        
    def update_rating(self, new_rating):
        self.rating = new_rating
        
movie1 = Movie("News", "citizen", 2025 , 3.)
movie1.display_info()
movie2 = Movie("Documentary", "allan", 2024, 5.)
movie2.display_info()
movie2.update_rating(4.)
movie1.display_info()
movie2.display_info()
        