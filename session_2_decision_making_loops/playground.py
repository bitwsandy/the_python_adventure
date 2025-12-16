
correct_username = "admin"
correct_password = "admin@123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username or password == correct_password:
    if username == correct_username :
        if password == correct_password :
            print("LOGIN SUCCESSFUL")
        else:
            print("INCORRECT PASSWORD")
    else:
        print("INCORRECT USERNAME")
else :
    print("INCORRECT USERNAME AND PASSWORD")