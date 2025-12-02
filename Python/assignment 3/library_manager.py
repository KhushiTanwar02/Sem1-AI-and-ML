#=========================================
# Name=Khushi
# date=26-11-25
# batch=b.tech CSE(AI/ML)
# title=librarymanager
#=========================================
#Task 1: make a book class 
class book:
    def __init__(self,title,author,isbn,status):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.status=status

    def __str__(self):
        return(f"{self.title} by {self.author} (ISBN : {self.isbn} - {self.status})")
    
    def to_dict(self):
        return{
            "title":self.title,
            "author":self.author,
            "isbn":self.isbn,
            "status":self.status
        }
    
    def issue(self):
        if self.status=="available":
            self.status="issued"
            print(True)
        else:    
            print(False)
        
    def return_book(self):
        if self.status=="issued":
            self.status="available"
            print(True)
        print(False)

    def available(self):
        print(self.status == "available")
    


class LibraryInventory:
    def __init__(self):
        self.book=[]

    def add_book(self,book):
        self.book.append(book)

    def search_by_title(self,title):
        for book in self.book:
            if book.title==title:
                print (book)
                return
            print(None)

    def search_by_isbn(self,isbn):
        for book in self.book:
            if book.isbn==isbn:
                print (book)
                return
            print(None)

    def display_all(self):
        print(self.book)

#Task 3:Implement functionality to save the library inventory to a file and load it back.


def save_to_file(self,filename):
        try:
            with open (filename,'w') as file:
                    for book in self.book:
                        file.write(f"{book.title},{book.author},{book.isbn},{book.status}\n")
        except Exception as e:
            print(f"Error saving to file: {e}")
    
def load_from_file(self,filename):
        try:
            with open (filename,'r') as file:
                    for line in file:
                        title,author,isbn,status=line.strip().split(',')
                        book_obj=book(title,author,isbn,status)
                        self.book.append(book_obj)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading from file: {e}")

#Task 4:Implement a simple interactive command-line interface (CLI) to interact with the library inventory system.
def interactive_cli():
    inventory= LibraryInventory()
    while True:
        print("Menu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book by Title")
        print("6. Search Book by ISBN")
        print("7. Exit")
        choice=input("Enter your choice (1-7): ")
        
        if choice=='1':
            title=input("Enter book title: ")
            author=input("Enter book author: ")
            isbn=input("Enter book ISBN: ")
            status="available"
            new_book=book(title,author,isbn,status)
            inventory.add_book(new_book)
            print("Book added successfully.")
        
        elif choice=='2':
            isbn=input("Enter book ISBN to issue: ")
            for bk in inventory.book:
                if bk.isbn==isbn:
                    bk.issue()
                    break
            else:
                print("Book not found.")
        
        elif choice=='3':
            isbn=input("Enter book ISBN to return: ")
            for bk in inventory.book:
                if bk.isbn==isbn:
                    bk.return_book()
                    break
            else:
                print("Book not found.")
        
        elif choice=='4':
            inventory.display_all()
        
        elif choice=='5':
            title=input("Enter book title to search: ")
            inventory.search_by_title(title)
        
        elif choice=='6':
            isbn=input("Enter book ISBN to search: ")
            inventory.search_by_isbn(isbn)
        
        elif choice=='7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

#Task 5:Implement logging to track operations and errors.
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def log_example():
    try:
        logging.info("This is an info message.")
        # Simulate an error
        1 / 0
    except ZeroDivisionError as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Execution completed.")

if __name__ == "__main__":
    interactive_cli()
    log_example()