def add_prices(books):
    #total = 0
    for book in books:
        #total = book + books
        total += book
        return total

print(add_prices([1,2,3]) == 6)