from pathlib import Path
from cryptography.fernet import Fernet

folder = Path("D:\\Ameng\\Python Project\\Project-Based-Learning\\Password-Manager")
file_name = "password.txt"
key_name = "key.key"
path_file = folder / file_name
key_file = folder / key_name

folder.mkdir(parents=True, exist_ok=True)

# ====================================================
"""
def write_key():
    key = Fernet.generate_key()
    with open(key_file, "wb") as key_f:
        key_f.write(key)
"""

def load_key():
    file = open(key_file, "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open(path_file, "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user} | Password: {(fer.decrypt(passw.encode())).decode()}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open(path_file, "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

while True:
    mode = input("Would you like to add a new password or view exsting ones (add/view) or press q to quit? ")
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid input!")