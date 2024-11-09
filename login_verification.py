#Verification

info = {
    "sanika": "password",
    "rohit": "123",
    "anuradha": "jadhav"
}

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")


def login_system(input_username, input_password):
    if input_username in info and info[input_username] == input_password:
        print("Login successful!")
        
    else:    
        print("Invalid username or password.")

login_system(input_username,input_password)
