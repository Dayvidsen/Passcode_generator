import random
import string
from datetime import datetime

def generate_passcode(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    passcode = ''.join(random.choice(characters) for i in range(length))
    return passcode

def store_passcode(passcode):
    with open("passcodes.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {passcode}\n")

if __name__ == "__main__":
    new_passcode = generate_passcode()
    store_passcode(new_passcode)
import random
import string
from datetime import datetime

def generate_passcode(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    passcode = ''.join(random.choice(characters) for i in range(length))
    return passcode

def store_passcode(passcode):
    with open("passcodes.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {passcode}\n")

if __name__ == "__main__":
    new_passcode = generate_passcode()
    store_passcode(new_passcode)

