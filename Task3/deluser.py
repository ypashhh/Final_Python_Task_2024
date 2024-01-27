from password_utils import get_usernames

def deluser(username, filename="passwd.txt"):
    lines = []
    user_deleted = False

    # Open the file in read mode to check for the user to delete
    with open(filename, "r") as file:
        for line in file:
            # Check if the line starts with the specified username
            if line.startswith(f"{username}:"):
                print("User Deleted.")
                user_deleted = True
            else:
                
                lines.append(line)

    # If the user was deleted, overwrite the file with the updated lines
    if user_deleted:
        with open(filename, "w") as file:
            file.writelines(lines)
    elif not user_deleted:
        # If the user was not found, inform the user
        print("User not found. Nothing changed.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Get user input for the username to delete
    username_to_delete = input("Enter username to delete: ")
    
    # Call the deluser function with the provided username to delete the user
    deluser(username_to_delete)
