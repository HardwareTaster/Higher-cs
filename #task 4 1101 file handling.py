#task 4 1101 file handling
names = ["John","Joan","Mark","Michael"]
birthmonths = ["March", "April", "December", "July"]
ages = [23,35,23,8]

with open("file handlers/names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(names[counter] + ", " + birthmonths[counter] + ", " +str(ages[counter])+"\n")
