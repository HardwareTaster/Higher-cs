#temps program 4 
#program 4
alltemps = []
from dataclasses import dataclass
@dataclass
class temperature():
    day: str = ""
    dayTemp: float = 0.0

def find_day():
    day = input("enter the day")
    return day

def get_temps():
    temperature = float(input("enter temperature"))
    while temperature <-20 or temperature > 50:
        print("error, temperature must be between -20 and 50 degrees celcius")
        temperature = float(input("enter temperature"))
    return temperature

def display_temperatures(day):
    for i in range (14):
        print(day[i].dayTemp)

def findmaxmin(day):
    max = day[0].dayTemp
    for i in range(1,len(day)):
        if day[i].dayTemp>max:
            max = day[i].dayTemp
    print("The highest temperature was", max, "degrees")
    min = day[0].dayTemp
    for i in range(1,len(day)):
        if day[i].dayTemp<min:
            min = day[i].dayTemp
    print("The lowest temperature was", min, "degrees")

def avg(temps):
    counter = 0
    for i in range (len(temps)):
        counter+= temps[i]
    avg = counter/len(temps)
    print(avg)


daydetails= [temperature() for i in range (14)]
for index in range (14):
    daydetails[index].day = find_day()
    daydetails[index].dayTemp = get_temps()
    alltemps.append(daydetails[index].dayTemp)
print (alltemps)
findmaxmin(daydetails)
avg(alltemps)
