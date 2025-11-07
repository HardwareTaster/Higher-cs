#temperatures file handles 1101

items = []
temperatures = []
counter = 0
with open ("file handlers/temps.txt") as rfile:
    line = rfile.readline().rstrip('\n')
    print(line)
    while line:
        temperatures.append(line)
        line = rfile.readline().rstrip('\n')

for i in range (0,len(temperatures)):
    counter+=int(temperatures[i])
avgtemp = counter/len(temperatures)
print(avgtemp)