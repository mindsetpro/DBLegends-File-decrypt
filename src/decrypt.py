import os
import sys

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

def main():
    # Get the folder path where the executable is located
    folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
  
    target_file = '89bb4eb5637df3cd96c463a795005065'
    for file_name in os.listdir(folder_path):
        if file_name.startswith(target_file):
            target_file_path = os.path.join(folder_path, file_name)
            break
    else:
        print(f"The target file ({target_file}) was not found in the folder '{folder_path}'.")
        input("Press Enter to exit...")
        sys.exit(1)

    try:
        decrypt_file(target_file_path)
        print(f"File '{os.path.basename(target_file_path)}' decrypted successfully.")
    except Exception as ex:
        print(f"An error occurred: {ex}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
