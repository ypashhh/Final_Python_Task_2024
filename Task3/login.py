from password_utils import verify_user, verify_password
import getpass
def login(username, password, filename="passwd.txt"):
    # Retrieve the stored password for the specified username
    stored_password = get_stored_password(username, filename)
    
    # Check if the username is valid and the provided password matches the stored password
    if verify_user(username, filename) and verify_password(password, stored_password):
        print("Access granted.")
    else:
        print("Access denied.")

def get_stored_password(username, filename="passwd.txt"):
    # Open the file and search for the stored password associated with the specified username
    with open(filename, "r") as file:
        for line in file:
            parts = line.split(":")
            # Check if the username in the current line matches the specified username
            if parts[0] == username:
                # Return the stored password (third part of the line) after stripping whitespace
                return parts[2].strip()
    
    return None

# Check if the script is being run as the main program
if __name__ == "__main__":
    user_login = input("User: ")
    password_login =getpass.getpass("Password: ")
    
    # Call the login function with the provided username and password for authentication
    login(user_login, password_login)
