#program 1
name = "Ada"
if name == "Ada":
    print("Hello Ada")
else:
    print("I don't recognise you")

#program 2 
name = input("what is your name")
if name == "John":
    print("Hello John")
else:
    print("Hello"+ name)

#program 3 
food = input("what is your favourite food")
if food == "pizza":
    print("An excellent choice!")
else:
    print("i don't think we can be friends")

#program 4 
food = input("what is your favourite food")
for index in range(5):
    print("My favourite food is"+ food)