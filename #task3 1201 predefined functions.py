#task3 1201 predefined functions
password = input("enter password")
while (ord(password[0:1])<65 or ord(password[0:1])>90) or (ord(password[-1])<35 or ord(password[-1])>37):
    print("the first letter must be a capital letter and the password must end in #, $, or %")
    password = input("enter password")