#assignment
def reader():
    company = []
    numEmployees = []
    ceoSalary = []
    with open("file handlers/companies.csv") as rfile:
        line = rfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            company.append(items[0])
            numEmployees.append(items[1])
            ceoSalary.append(items[2])
            line = rfile.readline().rstrip('\n')
    return company, numEmployees, ceoSalary


def findMaxPos(array):
    max = array[0]
    position = 0
    for i in range(1,len(array)):
        if array[i]>max:
            max = array[i]
            position = i
    return position

company,numEmployees, ceoSalary = reader()
print(company)
company = input("enter name of the company")
found = False
position = findMaxPos(numEmployees)
print(position)