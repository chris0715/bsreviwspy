from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import csv
import os

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine)) 

def main():
    list_of_authors = set()
    list_of_books = []
    print('I am working just fine!')
    file =  open('books.csv')
    mreader = csv.reader(file)
    for isbn, title, author, year in mreader:
      list_of_books.append({ "isbn": isbn, "title": title, "released": year })
      list_of_authors.add(author)
    for item in list_of_authors:
      db.execute('INSERT INTO author (name) values (:val)', { "val": item })
    for book in list_of_books:
      db.execute('INSERT INTO book (isbn, name, released) values (:isbn, :title, :released )',  book)
    db.commit()
main()