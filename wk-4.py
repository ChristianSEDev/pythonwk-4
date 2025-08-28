# 1. Opening the input file in read mode
with open("input.txt", "r") as infile:
    input_content = infile.read()

# Modifying the content
modified_content = input_content.upper()

# Open the output file in write mode
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

# 2. Asking the user to enter a filename
filename = input("Enter the filename: ")

try:
    # Prevent overwriting output.txt if user enters that filename
    if filename == "output.txt":
        print("Warning: You are trying to read the output file.")
    with open(filename, "r") as file:
        file_content = file.read()
        print(file_content)

# Handle the case where the file doesn't exist
except FileNotFoundError:
    print("Error: File not found.")

# Handle other input/output errors
except IOError:
     print("Error: Cannot read the file.")
