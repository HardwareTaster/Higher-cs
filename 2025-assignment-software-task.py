#record structure
from dataclasses import dataclass
@dataclass
class person():
    orderNum:int = 0
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
            orders[counter].rating= (items[5])
            counter += 1
            line = readfile.readline().rstrip('\n')
    return orders

def findpos(orders):
    position = -1
    index = 0
    month = input("enter month with 3 letters eg Nov with first letter as a capital")
    while position == -1 and index<len(orders):
        if orders[index].date[3:5] == month and orders[index].rating == 5:
            position = index
    return position
#main program
orders = readfromfile()
position = findpos(orders)
print(position)
#writedetails(orders, position)
#display(orders)