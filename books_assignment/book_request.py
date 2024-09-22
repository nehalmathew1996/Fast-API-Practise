from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id:int
    title:str = Field(default = 'None', title='name_of_book', max_length = 50)
    author:str
    rating:float

