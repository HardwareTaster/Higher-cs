#task 2 1201

def replace_letter(animal):
  if ord(animal[0])>=97 and ord(animal[0])<=122:
    newletter = chr(ord(animal[0])-32)
    newanimal = newletter+animal[1:]
    print(newanimal)
  else:
    print(animal)
  
animal = input("enter name of the animal in lowercase please")
replace_letter(animal)
