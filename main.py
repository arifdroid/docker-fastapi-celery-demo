import os

import uvicorn
from dotenv import load_dotenv
from fastapi import Body, FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from celery_worker import create_task, demo_scrape_data, scrape_data
from fastapi.responses import JSONResponse

from models import Author
from models import Author as ModelAuthor
from models import Book
from models import Book as ModelBook
from sampleSCVload import load_csv
from schema import Author as SchemaAuthor
from schema import Book as SchemaBook

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/load-csv")
def root():
    sample_csv = load_csv()
    return JSONResponse({"Result": sample_csv})


@app.get("/bankstatement")
def get_bank_statement():
    print("scraping 00")
    data = scrape_data.delay()
    return {"message": data}


@app.get("/demo-scrape")
def get_scraping_demo():
    print("scraping demo 00")
    data = demo_scrape_data.delay()
    return {"message": 'demo only'}


@app.post("/ex1")
def run_task(data=Body(...)):
    amount = int(data["amount"])
    x = data["x"]
    y = data["y"]
    task = create_task.delay(amount, x, y)
    return JSONResponse({"Result": task.get()})


@app.post("/add-book/", response_model=SchemaBook)
def add_book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating,
                        author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.post("/add-author/", response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


@app.get("/books/")
def get_books():
    books = db.session.query(Book).all()

    return books


# @app.post("/user/", response_model=SchemaUser)
# def create_user(user: SchemaUser):
#     db_user = ModelUser(
#         first_name=user.first_name, last_name=user.last_name, age=user.age
#     )
#     db.session.add(db_user)
#     db.session.commit()
#     return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
