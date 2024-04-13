# starszenkai.py
# made by mindsetpro

import json

# Function to decrypt a file
def decrypt_file(file_path):
    # Read file into memory
    with open(file_path, 'rb') as file:
        file_bytes = bytearray(file.read())

    # Decrypt the bytes
    for i in range(len(file_bytes)):
        file_bytes[i] = (~file_bytes[i] + 256) & 0xFF

    # Write back to file
    with open(file_path, 'wb') as file:
        file.write(file_bytes)

# Function to encrypt a file
def encrypt_file(file_path):
    # Read file into memory
    with open(file_path, 'rb') as file:
        file_bytes = bytearray(file.read())

    # Encrypt the bytes
    for i in range(len(file_bytes)):
        file_bytes[i] = (~file_bytes[i] + 256) & 0xFF

    # Write back to file
    with open(file_path, 'wb') as file:
        file.write(file_bytes)

# Function to edit counts
def edit_counts(data, threshold):
    for key, value in data.items():
        if isinstance(value, dict):
            if key.startswith("characterShards_") or key.startswith("characterPlentyShards_"):
                edit_counts(value, threshold)
            elif key == "count":
                if value < threshold:
                    data[key] = threshold

# Read and decrypt the file
file_path = "89bb4eb5637df3cd96c463a795005065"
decrypt_file(file_path)

# Read decrypted JSON data
with open(file_path, 'r') as file:
    decrypted_data = json.load(file)

# Edit counts
edit_counts(decrypted_data, 9999)  # Edit counts below 9999
edit_counts(decrypted_data, 7000)  # Edit counts below 7000

# Write back to file
with open(file_path, 'w') as file:
    json.dump(decrypted_data, file, indent=4)

print("Counts edited successfully.")

# Encrypt the file again
encrypt_file(file_path)

print("File encrypted successfully.")
