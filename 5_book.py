''' Check List of Books. Allow user to 
issue a book
return a book
check list
impart fine of rs. 1 after 15 days
veiw available books'''

import json


with open("books.json", "r") as file:
    books = json.load(file)


# for book in books:
#     print(book)


def checkAvalibility():
    pass


def issueBook():
    print("Issue Book ......")
    try:
        id = int(input("Enter the book id"))
    except:
        print("Book not found")
    
    for book in books:
        if book[id] == id:
            if book["availability"] == True:
                    books["availability"] = False  
                    print(f"Book '{books['title']}' has been issued successfully.")
            else:
                print(f"Book '{books['title']}' is NOT available.")
            break
        else:
            print("Book not found.")

        with open("books.json", "w") as file:
            json.dump(books, file, indent=4)



print("------------------------------Welcome to Book App------------------------------------")
print("Press 1 to issue a book \nPress 2 to retrun a book \nPress 3 to Check List of books \nPress 4 to fine a person \nPress 5 to View available books")
try:
    inp = int(input("Enter the option: "))
except:
    print("Wrong input")

if inp == 1:
    issueBook()
