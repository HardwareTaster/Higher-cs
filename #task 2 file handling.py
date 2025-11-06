#task 2 file handling
import time
#open file
with open("file handlers/newfile.txt","w") as writefile:
    writefile.write("Anton artikov, python-blue, February")
    time.sleep(1)
