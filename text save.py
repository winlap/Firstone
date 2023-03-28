import os

# Define the file path where user data will be stored
FILE_PATH = "userdata.txt"

# Function to check if a user exists in the user data file
def user_exists(username):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            for line in f:
                if line.strip().split(":")[0] == username:
                    return True
    return False

# Function to create a new user account
def create_account(username, password):
    with open(FILE_PATH, "a") as f:
        f.write(f"{username}:{password}\n")

# Function to authenticate a user
def authenticate(username, password):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and password == stored_password:
                    return True
    return False

# Function to save text to a file
def save_text(username, text):
    filename = f"{username}.txt"
    with open(filename, "w") as f:
        f.write(text)

# Function to load text from a file
def load_text(username):
    filename = f"{username}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return ""

# Main program loop
while True:
    choice = input("Do you want to login (l) or sign up (s)? ")
    if choice == "s":
        username = input("Enter a username: ")
        if user_exists(username):
            print("That username is already taken.")
            continue
        password = input("Enter a password: ")
        create_account(username, password)
        print("Account created successfully.")
    elif choice == "l":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if authenticate(username, password):
            print("Login successful.")
            print("\n1.Enter text\n2.Show written text")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                text = input("Enter some text: ")
                save_text(username, text)
                print("Text saved successfully.")
            else:
                print("Your saved text is:")
                print(load_text(username))
        else:
            print("Login failed. Please try again.")
    else:
        print("Invalid choice. Please try again.")
