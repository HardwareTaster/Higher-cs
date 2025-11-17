# 805Task3.py
# Standard Algorithms - Linear Search & Counting Occurrences

# Investigate and modify

def getTargetCharacter():
  target = input("Enter the character you are looking for")

  return target

def getCharacters():
  characters = ["Desperate Dan", "Numbskulls", "Dennis the Menace", "Minnie the Minx", "Walter", "Gnasher", "Billy Whizz"]

  return characters

def findCharacterPosition(oneToFind):
    found = False
    foundPosition = -1
    for i in range(len(characters)):
        if characters[i]==oneToFind:
            found = True
            foundPosition = i
    # FINISH OFF THIS CODE
    if found == True:
        print("the character was found at" , foundPosition)
    else:
        print("the character was not found")


#. *************MAIN*************

target = getTargetCharacter()
characters = getCharacters()
foundPosition = findCharacterPosition(target)
