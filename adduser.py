import hashlib
import getpass

# write_user_data(user_data, file_path)

#     Writes user data to a specified file.
#     Parameters:
#         user_data (list): A list of user data, where each user is represented as a list [username, full_name, hashed_password].
#         file_path (str): The path to the file where user data will be written.
#     Returns: None
#     Note: This function overwrites the existing content of the file.


def write_user_data(user_data, file_path):
    with open(file_path, 'w') as file:
        for user in user_data:
            file.write(':'.join(user) + '\n')


# read_user_data(file_path)
    #     Reads user data from a specified file.
    #     Parameters:
    #         file_path (str): The path to the file containing user data.
    #     Returns: A list of user data, where each user is represented as a list [username, full_name, hashed_password].
    #     Exceptions:
    #         FileNotFoundError: If the specified file does not exist, an empty list is returned
            

def read_user_data(file_path):
    try:
        with open(file_path, 'r') as file:
            user_data = [line.strip().split(':') for line in file]
        return user_data
    except FileNotFoundError:
        return []
    
    # hash_password(password)

#     Hashes a password using the SHA-256 algorithm.
#     Parameters:
#         password (str): The password to be hashed.
#     Returns: A hexadecimal string representing the hashed password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# This function adds a new user to the user database. It reads existing user data from a specified file, checks if the provided username already exists, and appends the new user's information if the username is unique. The user's password is hashed using the SHA-256 algorithm before being stored.

# Function: add_user(username, full_name, password, file_path)

#     Adds a new user to the user database.
#     Parameters:
#         username (str): The desired username for the new user.
#         full_name (str): The full name of the new user.
#         password (str): The password for the new user.
#         file_path (str): The path to the file storing user data.
#     Returns: None
#     Note: If the provided username already exists in the user database, the function prints an error message and does not add the user. Otherwise, it adds the new user to the database and prints a success message.


def add_user(username, full_name, password, file_path):
    if not username or not full_name or not password:
        print("Error: Username, full name, and password cannot be empty.")
        return

    user_data = read_user_data(file_path)
    hashed_password = hash_password(password)
    new_user = [username, full_name, hashed_password]

    for user in user_data:
        if user[0] == username:
            print(f"Error: User '{username}' already exists. Choose a different username.")
            return

    user_data.append(new_user)
    write_user_data(user_data, file_path)
    print("User created")
# Exception handling block to catch and handle errors
try:
    username = input("Enter new username: ").strip()
    full_name = input("Enter real name: ").strip()
    password = getpass.getpass("Enter password: ").strip()
    file_path = 'passwd.txt'
    add_user(username, full_name, password, file_path)
except Exception as e:
     # Print an error message if an exception occurs during user creation
    print(f"An error occurred: {e}")
