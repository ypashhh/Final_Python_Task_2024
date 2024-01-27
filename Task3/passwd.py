from password_utils import encrypt_password, verify_user, verify_password, get_usernames
import getpass
def passwd(username, current_password, new_password, confirm_password, filename="passwd.txt"):
    # Initialize an empty list to store lines from the file and a flag to track if the password was changed
    lines = []
    password_changed = False

    # Open the file in read mode to check for the specified username and current password
    with open(filename, "r") as file:

        for line in file:
            # Split the line into parts using colon (':') as a separator
            parts = line.split(":")
            
            # Check if the line corresponds to the specified username and the current password is valid
            if parts[0] == username and verify_password(current_password, parts[2]):
                # Check if the new password matches the confirmation password
                if new_password == confirm_password:
                    # Encrypt the new password and append the updated line to the list
                    encrypted_password = encrypt_password(new_password)
                    lines.append(f"{username}:{parts[1]}:{encrypted_password}\n")
                    print("Password changed.")
                    password_changed = True
                else:
                    # Inform the user if the new passwords do not match
                    print("New passwords do not match. Nothing changed.")
            else:
                # If the line does not match the specified username, add it to the list
                lines.append(line)

    # If the password was changed, overwrite the file with the updated lines
    if password_changed:
        with open(filename, "w") as file:
            file.writelines(lines)
    elif not password_changed and not verify_user(username, filename):
        
        print("User not found or current password is invalid. Nothing changed.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    
    username_to_change = input("Enter username to change password: ")
    current_password = getpass.getpass("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm Password: ")

    # Call the passwd function with the provided information to change the password
    passwd(username_to_change, current_password, new_password, confirm_password)
