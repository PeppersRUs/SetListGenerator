import random

# Song list of available songs, repertoire
rt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
setLength = None
setList = []

def lengthCheck(length):
    while length > (rt.__len__()):
        print("You do not have that many songs! Please try again.")
        length = int(input("How many songs would you like to play?: "))
    return

def populateSet(length):
    count = 0
    while count < setLength:
        # Generate random song from the repertoire
        song = random.choice(rt)
        # Check to make sure the song isnt alreaedy in the setlist
        if setList.count(song) == 0:
            setList.append(song)
            count = count + 1
        elif setList.count(song) > 0:
            count = count
    return

def printSet(list):
    for song in setList:
        print(song)
    return

# Get the length

setLength = int(input("How many songs would you like to play?: "))

# Make sure the set length isn't longer than the repertoire

lengthCheck(setLength)

# Populate the list!

populateSet(setLength)

# Print out setlist

printSet(setList)



input()

