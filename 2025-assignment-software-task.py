#record structure
from dataclasses import dataclass
@dataclass
class person():
    orderNum:str = ""
    date:str = ""
    email:str = ""
    option:str = ""
    cost:float = 0.0
    rating:int = 0

#subprograms
def readfromfile():
    with open("orders.txt") as readfile:
        counter = 0
        line = readfile.readline().rstrip('\n')
        orders = [person() for index in range (505)]
        while line:
            items = line.split(",")
            orders[counter].orderNum = (items[0])
            orders[counter].date = (items[1])
            orders[counter].email = (items[2])
            orders[counter].option = (items[3])
            orders[counter].cost = (items[4])
            orders[counter].rating= int(items[5])
            counter += 1
            line = readfile.readline().rstrip('\n')
    return orders

def findpos(orders):
    position = -1
    index = 0
    month = input("enter month with 3 letters eg Nov with first letter as a capital ")
    while position == -1 and index<len(orders):
        if orders[index].date[3:6] == month and orders[index].rating == 5:
            position = index
        index = index + 1
    return position

def writedetails(orders, position):
    with open ("winners.txt", "w") as wfile:
        if position >0:
            wfile.write (orders[position].orderNum + "," + orders[position].email + "," + orders[position].cost + "\n")
        else:
            print("no winner")

def countoption(orders,option):
    counter = 0
    for i in range (len (orders)):
        if orders[i].option == option:
            counter+=1
    return counter

def display(orders):
    delivered = countoption(orders,"Delivery")
    collected = countoption(orders, "Collection")
    print(delivered, "orders were delivered")
    print(collected, "orders were collected")
        
#main program
orders = readfromfile()

position = findpos(orders)
writedetails(orders, position)
display(orders)
