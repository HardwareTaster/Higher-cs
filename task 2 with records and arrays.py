#Records and Array of Records
#anton task 2

def enter_information(index):
    BMIdetails[index].height  = float(input("enter  height"))
    BMIdetails[index].weight  = float(input("enter weight"))
    BMIdetails[index].bmi = BMIdetails[index].weight / (BMIdetails[index].height ** 2)
    return BMIdetails [index]

from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)] 
for index in range(4):
    enter_information(index)
    
print(BMIdetails[0])
print(BMIdetails[1])
print(BMIdetails[2])
print(BMIdetails[3])

