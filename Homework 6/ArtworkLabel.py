# Homework 6.1                      ArtworkLabel.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 10/08/2021

# 11.8 LAB: Artwork label (modules)
# Define the Artist class in Artist.py with a constructor to 
# initialize an artist's information. The constructor should by 
# default initialize the artist's name to "None" and the years of 
# birth and death to 0.
#
# Define the Artwork class in Artwork.py with a constructor to 
# initialize an artwork's information. The constructor should by 
# default initialize the title to "None", the year created to 0, 
# and the artist to use the Artist default constructor parameter 
# values. Add an import statement to import the Artist class.
#
# Add import statements to main.py to import the Artist and 
# Artwork classes.
#
# Ex: If the input is:
#
# Pablo Picasso
# 1881
# 1973
# Three Musicians
# 1921
# the output is:
#
# Artist: Pablo Picasso (1881-1973)
# Title: Three Musicians, 1921
# If the input is:
#
# Brice Marden
# 1938
# -1
# Distant Muses
# 2000
# the output is:
#
# Artist: Brice Marden, born 1938
# Title: Distant Muses, 2000
 
from Artist import Artist
from Artwork import Artwork

if __name__ == "__main__":
    artistName = input("Please insert the artist's name: > ")
    birthYear = int(input("Please insert the artist's birth year: > "))
    deathYear = int(input("Please insert the artists year of death: > "))
    title = input("Please insert the title of the artwork: > ")
    yearCreated = int(input(""))

    artist = Artist(artistName, birthYear, deathYear)

    artwork = Artwork(title, yearCreated, artist)
  
    artwork.printInfo()