import hashlib

def write_user_data(user_data, file_path):
    # Writes user data to a file, overwriting existing content.
    try:
        with open(file_path, 'w') as file:
            for user in user_data:
                file.write(':'.join(user) + '\n')
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")

def read_user_data(file_path):
    # Reads user data from a file. Returns a list of user data or an empty list if the file does not exist.
    try:
        with open(file_path, 'r') as file:
            user_data = [line.strip().split(':') for line in file]
        return user_data
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []

def hash_password(password):
    # Hashes a password using SHA-256.
    return hashlib.sha256(password.encode()).hexdigest()

def delete_user(username, file_path):
    # Deletes a user by username from user data and writes the updated data to a file.
    if not username:
        print("Error: Username cannot be empty.")
        return

    user_data = read_user_data(file_path)

    for user in user_data:
        if user[0] == username:
            user_data.remove(user)
            write_user_data(user_data, file_path)
            print("User deleted")
            return

    print(f"Error: User '{username}' not found.")

# Get user input
username = input("Enter username: ").strip()
file_path = 'passwd.txt'

# Call the delete_user function
delete_user(username, file_path)
