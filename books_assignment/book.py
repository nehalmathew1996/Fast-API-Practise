# from pydantic import BaseModel

class Book:
    id:int
    title:str
    author:str
    rating:float 

    def __init__(self, id:int, title:str, author:str, rating:float):
        # super().__init__(id=id, title=title, author=author, rating=rating)
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating


