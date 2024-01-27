import codecs

def encrypt_password(password):
    # Function to encrypt a password using the ROT13 algorithm
    return codecs.encode(password, 'rot_13')

def get_usernames(filename):
    # Function to retrieve usernames from a file
    with open(filename, "r") as file:
        # Read all lines from the file and extract usernames by splitting each line at the colon (':') character
        lines = file.readlines()
        return [line.split(":")[0] for line in lines]

def verify_password(input_password, stored_password):
    # Function to verify if an input password, when encrypted, matches a stored (encrypted) password
    return encrypt_password(input_password) == stored_password.strip()

def verify_user(username, filename):
    # Function to verify if a given username exists in the list of existing usernames from the specified file
    existing_users = get_usernames(filename)
    return username in existing_users
