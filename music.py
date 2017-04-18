import csv
import time
import random

music = []                                                              #make list to carry imported elements from csv and to append new elements to it
with open('music.csv', 'r', newline='', encoding='utf-8-sig') as f:
   reader = csv.reader(f, delimiter='|')
   for row in reader:
       name = (row[0], row[1])                                          #make tuplet with artist and album name
       row[2] = int(row[2])                                             #change date of album to int
       information = (row[2], row[3], row[4])                           #make tuplet with year of release, genre and length
       name_and_information = (name, information)                       #make tuplet with 2 tuplets
       music.append(name_and_information)

print(music)

def menu():
    working = True
    while working:

        print("\nWelcome in the CoolMusic! Choose the action:\n")
        print("1) Add new album")
        print("2) Find albums by artist")
        print("3) Find albums by year")
        print("4) Find musician by album")
        print("5) Find albums by letter(s)")
        print("6) Find albums by genre")
        print("7) Calculate the age of all albums")
        print("8) Choose a random album by genre")
        print("9) Show the amount of albums by an artist")
        print("0 Exit")

        number = input("Enter a number: ")

        if number == '1':
            new_record()

        elif number == '2':
            album_by_artist()

        elif number == '3':
            album_by_year()

        elif number == '4':
            musician_by_album()
    
        elif number == '5':
            albums_by_letter()
        
        elif number == '6':
            albums_by_genre()

        elif number == '7':
            age_of_albums()
    
        elif number == '8':
            random_album_genre()
        
        elif number == '9':
            amount_of_albums_byartist()
        
        elif number == '0':
            print("Thank you! Goodbye!")
            break

        else:
            print(">>>>Enter only number from 0 to 9!<<<<\n")
            time.sleep(1.5)
    
        again = input('Do you want to try again? Put yes to confirm or any key to quit \n').lower()
        if again != 'yes':
            break

def new_record():
    print ('Enter an artist to a new record: ')
    artist = input().lower()
    print ('Enter an album to a new record: ')
    album = input().lower()
    print ('Enter a year to a new record: ')
    year = input().lower()
    while not year.isdigit():
        print ('This is not a year! Enter a year to a new record: ')
        year = input().lower()
        
    print ('Enter genre to a new record: ')
    genree = input().lower()
    print ('Enter a time to a new record: ')
    time = input().lower()


    z = artist + ' | ' + album + ' | ' + year + ' | ' + genree + ' | ' + time #creating new variable with set form to be exported to csv file
    with open('music.csv', "a") as add_record:
        add_record.write(z + "\n")

    music.append(((artist, album), (int(year), genree, time)))                #adding new elements to list music made at the begging of the program


def album_by_artist():
    albums_artist =[]
    done = False
    artist_album = input('Enter the name of artist: ')+ ' '
    for tuplee in music:
        if artist_album.lower() == tuplee[0][0].lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            art_alb = 'Album:' + album_name
            albums_artist.append(art_alb)
            done = True
    if done is True:     
        print('\nHere are all the albums made by this artist: ' + author)
        print('\n'.join(albums_artist))
    else:
        print('Artist is not known. Try again.')

def album_by_year():
    albums_artist =[]
    done = False
    album_year = input('Enter the year of album: ')
    for tuplee in music:
        if album_year.lower() == str(tuplee[1][0]).lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            art_alb = 'Album:' + album_name + ' | Artist: ' + author
            albums_artist.append(art_alb)
            done = True
    if done is True:     
        print('\nHere are all the albums made in this year: ')
        print('\n'.join(albums_artist))
    else:
        print('Year not found. Try again.')

def musician_by_album():
    albums_artist =[]
    done = False
    album_title = ' ' + input('Enter the album title: ') + ' '
    for tuplee in music:
        if album_title.lower() == str(tuplee[0][1]).lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            art_alb = 'Album:' + album_name + ' | Artist: ' + author
            albums_artist.append(art_alb)
            done = True
    if done is True:     
        print('\nThe album and it\'s author: ')
        print('\n'.join(albums_artist))
    else:
        print('Album not found. Try again.')

def albums_by_letter():
    albums_artist =[]
    done = False
    letters = input('Type letters that include in album: ')
    for tuplee in music:
        if letters.lower() in str(tuplee[0][1]).lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            art_alb = 'Album:' + album_name + ' | Artist: ' + author
            albums_artist.append(art_alb)
            done = True
    if done is True:     
        print('\nHere are all the albums containing these letters: ')
        print('\n'.join(albums_artist))
    else:
        print('Albums not found. Try again.')

def albums_by_genre():
    albums_artist =[]
    done = False
    genre = ' ' + input('Type the genre of albums you would like to search: ') + ' '
    for tuplee in music:
        if genre.lower() == (tuplee[1][1]).lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            art_alb = 'Album:' + album_name + ' | Artist: ' + author
            albums_artist.append(art_alb)
            done = True
    if done is True:     
        print('\nHere are all the albums from this genre: ')
        print('\n'.join(albums_artist))
    else:
        print('Genre not found. Try again.')

def age_of_albums():
    now_year = 2017
    agg_age = 0
    for album in music:
        album_year = int(album[1][0])
        age = now_year - album_year
        agg_age += age
    
    print(agg_age)

def random_album_genre():
    albums_artist =[]
    done = False
    genre = ' ' + input('Type the genre of albums: ') + ' '
    for tuplee in music:
        if genre.lower() == (tuplee[1][1]).lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            year = str(tuplee[1][0])
            art_alb = 'Album:' + album_name + ' | Artist: ' + author + ' | Year: ' + year
            albums_artist.append(art_alb)
            done = True
    if done is True:     
        print('\nHere are all the albums from this genre: ')
        print(random.choice(albums_artist))
    else:
        print('Genre not found. Try again.')

def amount_of_albums_byartist():
    amount = 0
    albums_artist =[]
    done = False
    artist_album = input('Type the author to show the amount of albums: ') + ' '
    for tuplee in music:
        if artist_album.lower() == (tuplee[0][0]).lower():
            author = tuplee[0][0]
            album_name = tuplee[0][1]
            albums_artist.append(album_name)
            amount += 1
            done = True
    if done is True:     
        print('\nThe amount of albums by the author: ' + author + 'is: ' + str(amount) + '\nThese are:')
        print('\n'.join(albums_artist))
            
    else:
        print('Author not found. Try again.')

menu()