# anton task 1 
from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)] # DECLARE BMIDetails(40) AS PERSON

BMIdetails[0].height  = 1.6
BMIdetails[0].weight  = 62.3
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height ** 2)

BMIdetails[1].height  = 1.23
BMIdetails[1].weight  = 43.3
BMIdetails[1].bmi = BMIdetails[1].weight / (BMIdetails[1].height ** 2)

BMIdetails[2].height  = 2.09
BMIdetails[2].weight  = 90.9
BMIdetails[2].bmi = BMIdetails[2].weight / (BMIdetails[2].height ** 2)

BMIdetails[3].height  = 1.12
BMIdetails[3].weight  = 70.2
BMIdetails[3].bmi = BMIdetails[3].weight / (BMIdetails[3].height ** 2)

print(BMIdetails[0])
print(BMIdetails[1])
print(BMIdetails[2])
print(BMIdetails[3])