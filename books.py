from fastapi import FastAPI

app= FastAPI()

BOOKS = [
    {'id':'1','title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'id':'2','title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'id':'3','title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'id':'4','title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'id':'5','title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'id':'6','title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def getBooks():
    return BOOKS

@app.get("/books/{id}")
async def get_book(id: str):
    for book in BOOKS:
        if id == book['id']:
            return book
