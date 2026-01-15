import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

print("Program started")

file_path = input("Enter the file path: ")

if not os.path.exists(file_path):
    print("File does not exist.")
else:
    original_hash = calculate_hash(file_path)
    print("Original Hash:", original_hash)

    input("Modify the file and press Enter...")

    new_hash = calculate_hash(file_path)
    print("New Hash:", new_hash)

    if original_hash == new_hash:
        print("File integrity maintained.")
    else:
        print("File integrity compromised.")