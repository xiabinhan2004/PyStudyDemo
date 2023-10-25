book=["1111","2222","3333","4444","5555"]
while(True):
    book_in=input()
    if "show"==book_in:
        print(book)
        continue
    if "exit"==book_in:
        break
    contain=False
    for i in book:
        if book_in==i:
            contain=True
    if contain == True:
        book.remove(book_in)
    else:
        book.append(book_in)
    
    