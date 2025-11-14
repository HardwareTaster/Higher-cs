#reading from a file with multiple arrays

def read_from_file_into_parallel_arrays():
    company = []
    numEmployees = []
    ceoSalary = []
    with open(filePath+'companies.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
    return company, numEmployees, ceoSalary