import hashlib  # for hashing passwords
import getpass  # for hiding passwords

def read_user_data(file_path):
    # read user data from file and return as list of lists
    try:
        with open(file_path, 'r') as file:
            user_data = [line.strip().split(':') for line in file]
        if not user_data:
            print("Error: User data file is empty.")
        return user_data
    except FileNotFoundError:
        return []

def hash_password(password):
    # hash password using SHA-256 and return hex digest
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password, file_path):
    # check if username and password match user data in file
    if not username or not password:
        print("Error: Username and password cannot be empty.")
        return

    user_data = read_user_data(file_path)

    for user in user_data:
        stored_username, stored_password = user[0], user[2]
        if stored_username == username and stored_password == hash_password(password):
            print("Access granted")
            return
    print("Access denied")

username = input("Enter your username: ").strip()
password = getpass.getpass("Enter your password: ").strip()
file_path = 'passwd.txt'
login(username, password, file_path)
