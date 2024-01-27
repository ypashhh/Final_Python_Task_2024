from password_utils import encrypt_password, get_usernames
import getpass
def adduser(username, realname, password, filename="passwd.txt"):
    # Open the specified file in append mode to add a new user
    with open(filename, "a") as file:
        # Get the list of existing usernames from the file
        existing_users = get_usernames(filename)
        
        # Check if the new username already exists
        if username in existing_users:
            print("Cannot add. Most likely username already exists.")
        else:
            # Encrypt the provided password using the password_utils module
            encrypted_password = encrypt_password(password)
            
            # Write the new user information to the file in the format: username:realname:encrypted_password
            file.write(f"{username}:{realname}:{encrypted_password}\n")
            print("User Created.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    new_username = input("Enter your new username: ")
    new_realname = input("Enter your real name: ")
    new_password = getpass.getpass("Enter your password: ")
    
    # Call the adduser function to add the new user
    adduser(new_username, new_realname, new_password)
