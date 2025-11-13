#file handles + standard algorithms giga programm
from random import *

numbers = []

def random_numbers():
  for x in range(20):
    numbers.append(randrange(1,30))
  return numbers

def add_to_file(numbers):
    with open("file handlers/numbers.txt","w") as wfile:
        for i in range(0, len(numbers)):
            wfile.write(str(numbers[i])+"\n")

def finding_max():
   numbers = []
   with open("file handlers/numbers.txt") as rfile:
        line = rfile.readline().rstrip('\n')
        while line:
            numbers.append(line)
            line = rfile.readline().rstrip('\n')
        max = numbers[0]
        for i in range(1,len(numbers)):
            if numbers[i]>max:
                max = numbers[i]
        return max

def finding_min():
   numbers = []
   with open("file handlers/numbers.txt") as rfile:
        line = rfile.readline().rstrip('\n')
        while line:
            numbers.append(line)
            line = rfile.readline().rstrip('\n')
        minimum = numbers[0]
        for i in range(1,len(numbers)):
            if numbers[i]<minimum:
                minimum = numbers[i]
        return minimum
   
def count_occurences(number):
    numbers = []
    occurrences = 0
    with open("file handlers/numbers.txt") as rfile:
        line = rfile.readline().rstrip('\n')
        while line:
            numbers.append(line)
            line = rfile.readline().rstrip('\n')
        print(numbers)
        for x in range(0,len(numbers)):
            if numbers[x] == str(number):
                occurrences = occurrences + 1
        return occurrences





numbers = random_numbers()
add_to_file(numbers)
selector = int(input("enter 1 to find the max of the numbers, 2 to find the min of the numbers, and 3 to count occurences"))
while selector !=1 and selector !=2 and selector !=3:
    print("error, select 1, 2 or 3")
    selector = int(input("enter 1 to find the max of the numbers, 2 to find the min of the numbers, and 3 to count occurences"))
if selector == 1:
    max=finding_max()
    print("the max value was:" , max)
elif selector == 2:
    min=finding_min()
    print("the min value was:",  min)
else:
    target_number = int(input("enter the number you would like to count the occurrences of (between 1 and 30)"))
    number = count_occurences(target_number)
    print("your number appeared", number , "times")