from dataclasses import dataclass
import os
import books


@dataclass
class Library:
  isCardHolder: bool
  balance: int
  hasPaid: bool
  hasBook: int
  
def hasLibraryCard(library: Library, action) -> None:
  if action == "y":
    library.isCardHolder = True
  elif action == "n":
    library.isCardHolder = False
    while not library.isCardHolder:
      action = input("You need a library card to get a book.\nWould you like to get one now? [Y]es, [N]o.\n").strip().lower()
      if action == "y":
        library.isCardHolder = True
        print("You now have a Library Card!")
      elif action == "n":
        print("Sorry, but you cannot check out a book without a library card.")
      else:
        print("Invalid choice")
  else:
    print("Invalid Choice, please choose Y, or N.")

def bookListCheckIn(bookList, action: int) -> None:
  new_action = action - 1
  bookList[new_action].is_checked_out = False

def bookListCheckout(bookList, action: int) -> None:
  new_action = action - 1
  bookList[new_action].is_checked_out = True
  
def booksByGenre(bookList) -> bool:
  isActionBack = False
  genre_type = input("> ").lower().strip()
  if genre_type == "fantasy":
    for i, book in enumerate(bookList):
      if book.genre == genre_type and not book.is_checked_out:
        print(f"{i+1}. {book.title}")
  if genre_type == "non-fiction":
    for i, book in enumerate(bookList):
      if book.genre == genre_type and not book.is_checked_out:
        print(f"{i+1}. {book.title}")
  if genre_type == "science-fiction":
    for i, book in enumerate(bookList):
      if book.genre == genre_type and not book.is_checked_out:
        print(f"{i+1}. {book.title}")
  if genre_type == "horror":
    for i, book in enumerate(bookList):
      if book.genre == genre_type and not book.is_checked_out:
        print(f"{i+1}. {book.title}")
  if genre_type == "back":
    isActionBack = True

  return isActionBack
     
def viewSynopsis(bookList, action) -> None:
  book_number = action - 1
  print(f"\n{bookList[book_number].title}\n\n{bookList[book_number].synopsis}")

def clear():
  os.system('clear')
    

def main():
  library = Library(False, 0, True, 0)
  running = True
  bookList = books.getBookList()
  
  while running:
    action = input("""\nWelcome to the BCCA-GI Library.
Please choose a number option below.
    
         1. Check in
         2. Check out
         3. View books
         4. Quit

> """).lower().strip()
    
    if action == "4": # quit
      running = False
      
    if action == "3": # View
      clear()
      #List books
      for  i, book in enumerate(bookList):
          print(f"{i+1}. {book.title} - [{book.genre}] - {'[Checked out]' if book.is_checked_out else '[Available]'}")
      action = input("Choose a book to view\n> ")
      if action.isdigit():
        action = int(action)
        viewSynopsis(bookList, action)
      else:
        print("Invalid Choice! Please choose a book number.")
      
    if action == "1": # Checking in
      clear()
      print("Return book")
      if library.hasBook == 0:
        print("There are no checked out books!")
        continue
      elif library.hasBook > 0:
        for i, book in enumerate(bookList):
          if book.is_checked_out:
            print(f"{i+1}. {book.title}")
      checkInAction = int(input("What's the book number that you would to check in?\n> "))
      bookListCheckIn(bookList, checkInAction)
      library.hasBook -= 1
       
    elif action == "2": # Checking Out
      if library.hasBook >= 2:
        print("Sorry you have too many books checked out right now, please return one to check out another book.")
        
      if not library.isCardHolder:
        action = input("Do you have a library card? [Y]es, [N]o\n> ").lower().strip()
        hasLibraryCard(library, action)
        
      if library.isCardHolder and library.hasBook < 2:
        print("What genre of book are you checking out? ")
        print("Fantasy\nHorror\nScience-Fiction\nNon-Fiction\nBack")
        
        isActionBack = booksByGenre(bookList)

        if isActionBack:
          continue
        
        checkOutAction = input("Please choose a book number to checkout, or go back.\n> ").lower().strip()
        if checkOutAction == "back":
          continue
        if checkOutAction.isdigit():
          checkOutAction = int(checkOutAction)
          bookListCheckout(bookList, checkOutAction)
          library.hasBook += 1
        else:
          print("Invalid Choice")

        

if __name__ == "__main__":
  main()