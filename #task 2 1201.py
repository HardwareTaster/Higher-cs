#task 2 1201
animal = input("enter name of the animal in lowercase please")

newletter = chr(ord(animal[0])-32)
newanimal = newletter+animal[1:]
print(newanimal)