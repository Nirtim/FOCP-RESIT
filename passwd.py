# Importing hashlib for password hashing and getpass for secure password input
import hashlib
import getpass

# Reads user data from a specified file and handles FileNotFoundError by returning an empty list
def read_user_data(file_path):
    try:
        with open(file_path, 'r') as file:
            user_data = [line.strip().split(':') for line in file]
        return user_data
    except FileNotFoundError:
        return []

# Writes user data to a specified file, overwriting existing content
def write_user_data(user_data, file_path):
    with open(file_path, 'w') as file:
        for user in user_data:
            file.write(':'.join(user) + '\n')

# Hashes a password using the SHA-256 algorithm
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Updates the password for a user in the user database; prints success or error message
def update_user(username, old_password, new_password, file_path):
    # Check if username, old password, or new password is empty
    if not username or not old_password or not new_password:
        print("Error: Username, old password, and new password cannot be empty.")
        return

    user_data = read_user_data(file_path)
    hashed_password = hash_password(new_password)

    for user in user_data:
        if user[0] == username and user[2] == hash_password(old_password):
            user[2] = hashed_password
            write_user_data(user_data, file_path)
            print("Password changed")
            return

    print("Invalid username or password")

# Get user input for updating the password and check if passwords match
username = input("Enter username: ").strip()
old_password = getpass.getpass("Enter old password: ").strip()
new_password = getpass.getpass("Enter new password: ").strip()
confirm_password = getpass.getpass("Confirm new password: ").strip()

# Check if new password and confirm password match
if new_password != confirm_password:
    print("Passwords do not match.")
    exit()

file_path = 'passwd.txt'
update_user(username, old_password, new_password, file_path)
