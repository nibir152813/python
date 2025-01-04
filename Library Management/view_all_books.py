
#def view_all_books(all_books):
   #if all_books != []:
        #for book in all_books:
            #print(f"Title :{book['title']} | Author: {book['author']} | ISBN {book['isbn']} | Year {book['year']} | price {book['price']} | Quantity {book['quantity']}")

        #else:
           # print("No Book found in All Books file")

import json

def view_all_books(all_books):
    with open("all_books.json","r") as fp:
        all_books = json.load(fp)

    if all_books != []:
        for book in all_books:
            print(
                f"Title :{book['title']} | Author: {book['author']} | ISBN {book['isbn']} | Year {book['year']} | price {book['price']} | Quantity {book['quantity']} |Book Added At:{book['bookAddedAt']} | Book last update At: {book['booklastupdated']}")

        else:
            print("No Book found. ")

