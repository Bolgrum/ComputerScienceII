# Homework 8.2                      PookInformation.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/29/2021

# 13.10 LAB: Book information (overriding member methods)
# Given the base class Book, define a derived class called 
# Encyclopedia. Within the derived Encyclopedia class, define a 
# printInfo() method that overrides the Book class' printInfo() 
# method by printing not only the title, author, publisher, and 
# publication date, but also the edition and number of volumes.
# 
# Ex: If the input is:
# 
# The Hobbit
# J. R. R. Tolkien
# George Allen & Unwin
# 21 September 1937
# The Illustrated Encyclopedia of the Universe
# James W. Guthrie
# Watson-Guptill
# 2001
# 2nd
# 1
# the output is:
# 
# Book Information:
# Book Title: The Hobbit
# Author: J. R. R. Tolkien
# Publisher: George Allen & Unwin
# Publication Date: 21 September 1937
# Book Information:
# Book Title: The Illustrated Encyclopedia of the Universe
# Author: James W. Guthrie
# Publisher: Watson-Guptill
# Publication Date: 2001
# Edition: 2nd
# Number of Volumes: 1
# Note: Indentations use 3 spaces.

class Book:
    def __init__(self, title, author, publisher, publicationDate):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publicationDate = publicationDate
   
    def printInfo(self):
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publicationDate)
        
class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publicationDate, edition, numberOfVolumes):
        Book.__init__(self, title, author, publisher, publicationDate) 
        self.edition = edition
        self.numberOfVolumes = numberOfVolumes

    def printInfo(self):
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publicationDate)
        print('   Edition:', self.edition)
        print('   Number of Volumes:', self.numberOfVolumes)

if __name__ == "__main__":
    title = input()
    author = input()
    publisher = input()
    publicationDate = input()
    
    encyclopediaTitle = input()
    encyclopediaAuthor = input()
    encyclopediaPublisher = input()
    encyclopediaPublicationDate = input()
    edition = input()
    numberOfVolumes = int(input())
    
    myBook = Book(title, author, publisher, publicationDate)
    myBook.printInfo()
    
    myEncyclopedia = Encyclopedia(encyclopediaTitle, encyclopediaAuthor, encyclopediaPublisher, encyclopediaPublicationDate, edition, numberOfVolumes)
    myEncyclopedia.printInfo()