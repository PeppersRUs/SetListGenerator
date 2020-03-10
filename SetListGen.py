import random, os, csv

# Next tasks -  1. Creating .csv file to store band repertoires
#               2. Must have create/write/read abilities
#               3. Create menu to navigate functions

#


# Song list of available songs, repertoire
rt = [["Romeo Indigo Romeo", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["Simon", 11, 22, 33, 44, 55, 66], ["Bob", 111, 222, 333, 444, 555]]
setLength = None
setList = []

# Create new nested list item for new act

def newAct():
    newActName = input("What is your act's name?: ")
    rt.append([newActName])
    return

# Edit repertoires

def modifyRepertoire(list):
    print("Choose an act to modify!:")
    for x in range(0, list.__len__()):
        print(str(x + 1) + ". " + (list[x][0]))

    # Select an act to modify

    actToMod = int(input("Press the corresponding number: ")) - 1

    # Return current stored songs

    print("Current songs in repertoire: ")
    for y in range(1, list[actToMod].__len__()):
        print(str(y) + ". " + str(list[actToMod][y]))

    # Give options to modify songs

    


    return
    
#  Check setlist length against repertoire length

def lengthCheck(length):
    while length > (rt.__len__()):
        print("You do not have that many songs! Please try again.")
        length = int(input("How many songs would you like to play?: "))
    return

#  Populate setList

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

# Print setList

def printSet(list):
    for song in setList:
        print(song)
    return

############ PROGRAM ############
# still to be tested
#modifyRepertoire(rt)

# Get the length

setLength = int(input("How many songs would you like to play?: "))

# Make sure the set length isn't longer than the repertoire

lengthCheck(setLength)

# Populate the list!

populateSet(setLength)

# Print out setlist

printSet(setList)



input()

