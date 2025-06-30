library=[]
while True:
    print("\nLibrary Management System:")
    print("1. Add a Book")
    print("2. Display All Books")
    print("3. Search for a Book")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Exit")
    num=int(input("Select the number= "))
    if num==1:
        book_id=int(input("Enter the ID= "))
        tittle=input("Enter the Title= ").lower()
        author=input("Enter the author details= ").lower()
        library.append({"id":book_id, "title":tittle, "author":author, "borrowed":False})
        print(f"{book_id} and {author} added sucessfully..!!")
    elif num==2:
        if library:
            print("Available boks are:- ")
            for book in library:
                status="borrowed" if book["borrowed"] else "Available"
                print(f"ID:{book['id']},title:{book['title']},author:{book['author']},status:{status}")
            else:
                print("No books available right now..!")
    elif num==3:
        search=input("Search the book= ").lower()
        found=False
        for book in library:
            if search in book["title"].lower() or search in book["author"].lower():
                status="borrowed" if book["borrowed"] else "Available"
                print(f"id:{book['id']}, title:{book['title']},author:{book['author']},status:{status}")
                found=True
        if not found:
            print("NO matching found")
    elif num==4:
        borrow=input("Enter the book").lower()
        for book in library:
            if book['id']==borrow:
                if not book['borrowed']:
                    book['borrowed']=True
                    print("Sucessfuly borrowed")
                else:
                    print("sorry not avaliable")
                    break
            else:
                print("invalid")
    elif num==5:
        return_book=input("Enter the book")
        for book in library:
            if book['id']==return_book:
                if not book['borrowed']:
                    book['borrowed']=False
                    print("Thanks for returning..!")
                else:
                    print("not returned")
            else:
                print("invalid")
    elif num==6:
        print("Thanks ..Good Bye..!")
        break
    else:
        print("Invalid input ..Try again")
