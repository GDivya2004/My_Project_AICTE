import cv2

# Load the encrypted image
image_path = r"C:\Users\lenovo\OneDrive\Documents\teddy.jpg"
img = cv2.imread(image_path)

# Check if the image is loaded correctly
if img is None:
    print("Error: Image file not found or unreadable!")
    exit()

# Load stored password from file
password_file = "mydoc.txt"  # Ensure this file exists in the correct location

try:
    with open(password_file, "r") as f:
        password = f.read().strip()  # Read and clean password
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()

# Dictionary to map bytes to characters
c = {i: chr(i) for i in range(256)}

# Get passcode from user
pas = input("Enter passcode for Decryption: ")

# Check if entered password matches stored password
if password == pas:
    message = ""
    n, m, z = 0, 0, 0  # Initialize indices

    while True:
        try:
            char_code = img[n, m, z]
            if char_code == 0:  # Stop when null character is found
                break
            message += c.get(char_code, "?")  # Add character to message
            z = (z + 1) % 3  # Cycle through RGB channels

            if z == 0:  # Move to next pixel
                m += 1
                if m >= img.shape[1]:  # Move to next row if end of row is reached
                    m = 0
                    n += 1
        except IndexError:
            print("Error: Reached image boundary unexpectedly.")
            break

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
