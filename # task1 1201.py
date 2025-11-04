# task1  1201
total =0
password = input("enter password")
for i in range(0,len(password)):
    total+= ord(password[i])
check = total%11
newpassword = password+str(check)
print(newpassword)