import os

def registration():
    Name = input("enter your name ")
    mobile = input("Enter your mobile number ")
    email = input("Enter youy email address ")
    password = input("Enter Password")

    last_four_digit = mobile[-4:]

    filename = Name + "_" + last_four_digit
    filepath = os.path.join("RegistrationData",filename)

    os.makedirs("RegistrationData", exist_ok=True)

    with open(filepath,"w") as f:
        f.write(Name + " " + mobile + " " + email + " " + password + "\n")
        print("Registered succesfully!!!")


def login():
   
    Name = input("Enter your name ")
    mobile = input("enter your mobile number ")
    pass1 = input("enter your password ")
    count = 0

    last_four_digit = mobile[-4:]
    filename = Name + "_" + last_four_digit

    filepath = os.path.join("RegistrationData", filename)
    with open(filepath,"r") as f:
        lines = f.readline()
        data = lines.split()
        username = data[0]  
        password = data[-1]

        # print(data[0])
        # print(data[-1])
        if username == Name:
            count+=1
        
        if password == pass1:
            count+=1
        
        if count==2:
            print("Login Successfully!!!")

            print("1:Account Details")
            print("2:update")
        
        else:
            print("Invalid username or password!!!")

def switch_case(choice):
    if choice == "1":
        registration()
        

    elif choice == "2":
        login()

print("1:Registration")
print("2.Login")
choice = input("ENTER YOUR CHOICE: ")
switch_case(choice)




