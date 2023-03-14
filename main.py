from typing import Optional
from fastapi import FastAPI

from enum import Enum

app = FastAPI()

BOOKS = {
            'book_1' : {'title': 'Title One' , 'author': 'Aurthor One'},
            'book_2' : {'title': 'Title Two' , 'author': 'Aurthor Two'},
            'book_3' : {'title': 'Title Three' , 'author': 'Aurthor Three'},
            'book_4' : {'title': 'Title Four' , 'author': 'Aurthor Four'},
            'book_5' : {'title': 'Title Five' , 'author': 'Aurthor Five'},
}

class directionName (str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def read_all_books(skip_book : Optional[str] = None ):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/books/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x

    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']

 

@app.put("/books/{book_name}")
async def update_book(book_name : str, book_title: str, book_aurthor:str):
    book_information = {'title': book_title, 'aurthor': book_aurthor}
    BOOKS[book_name] = book_information
    return book_information



@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book {book_name} deleted.'





@app.get("/books/mybook")
async def read_favourite_book():
    return {"book title": "My Favourite Book"}


@app.get("/directions/{direction_name}")
async def get_direction(direction_name : directionName):
    if direction_name == directionName.north:
        return{"Direction": direction_name,"sub": "Up"}
    if direction_name == directionName.south:
        return{"Direction": direction_name,"sub": "Down"}    
    if direction_name == directionName.east:
        return{"Direction": direction_name,"sub": "Right"}    
    if direction_name == directionName.west:
        return{"Direction": direction_name,"sub": "Left"}



@app.get("/books/{book_id}")
async def read_book(book_id : int):
    return {"book_title": book_id}