#task3 1101 file handling
items = []
names = []
marks = []
with open("file handlers/pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')
for i in range(0,len(names)):

    print(names[i],"-",marks[i])
