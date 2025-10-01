#parallel 1d arrays
#anton
#without subroutines:
    # names = []
    # testscores = []
    # for i in range (5):
    # 	name = input("enter your name")
    # 	testscore = input("enter your testscore")
    # 	names.append(name)
    # 	testscores.append(testscore)
    # print(names)
    # print(testscores)
#subroutines


def get_name():
    thisName = input("enter your name")
    return thisName

def get_testmark():
    thismark = int(input("enter your mark(0-100)"))
    while thismark < 0 or thismark > 100:
        print("error")
        thismark = int(input("enter your mark"))
    return thismark

def display_all(aName, aMark):
    for index in range(5):
        print(aName[index]+ " scored " + str(aMark[index]))


#top level design
name = []
mark = []
for index in range (5):
	name.append( get_name())
	mark.append(get_testmark())
display_all(name, mark)