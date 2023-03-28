import random
import string

def generate_password(length,uppercase,lowercase,digits,symbols):

    """"
    Generates a random password with the specified lwngth and character types
    """

    #define the character sets for each type of character.
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    #create a list of character sets to include in the password.
    char_sets = []
    if uppercase:
        char_sets.append(uppercase_chars)
    if lowercase:
        char_sets.append(lowercase_chars)
    if digits:
        char_sets.append(digit_chars)
    if symbols:
        char_sets.append(symbol_chars)

    #generate a password by randomly selecting characters from the selected character serts
    password_chars = []
    for i in range(length):
        char_set = random.choice(char_sets)
        password_chars.append(random.choice(char_set))

    #convert the list of characters to a string and return the password.
    password = ''.join(password_chars)
    return password

# prompt the user to enter the desired length and character types for the password
length = int(input("\nEnter the desired length of the password: "))
uppercase = input("\nInclude uppercase letters?[y/n]: ").lower() == 'y'
lowercase = input("\nInclude lowercase letters?[y/n]: ").lower() == 'y'
digits = input("\nInclude digits?[y/n]: ").lower() =='y'
symbols = input("\nInclude symbols?[y/n]: ").lower() =='y'

#generate and display the password.
password = generate_password(length,uppercase,lowercase,digits,symbols)
print("\nYour password is: ",password)