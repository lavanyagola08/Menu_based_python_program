import os
import sys

# Define the menu options
menu_options = {
    "1": "List files in current directory",
    "2": "Create a new file",
    "3": "Delete a file",
    "4": "Copy a file",
    "5": "Move a file",
    "6": "Rename a file",
    "7": "Quit"
}

# Print the menu options
def print_menu():
    for key, value in menu_options.items():
        print(f"{key}: {value}")

# Get the user's choice
def get_choice():
    choice = input("Enter your choice: ")
    return choice

# List files in current directory
def list_files():
    files = os.listdir(".")
    for file in files:
        print(file)

# Create a new file
def create_file():
    filename = input("Enter the name of the new file: ")
    with open(filename, "w") as f:
        f.write("")

# Delete a file
def delete_file():
    filename = input("Enter the name of the file to delete: ")
    os.remove(filename)

# Copy a file
def copy_file():
    source_filename = input("Enter the name of the source file: ")
    destination_filename = input("Enter the name of the destination file: ")
    with open(source_filename, "r") as source_file:
        with open(destination_filename, "w") as destination_file:
            destination_file.write(source_file.read())

# Move a file
def move_file():
    source_filename = input("Enter the name of the source file: ")
    destination_filename = input("Enter the name of the destination file: ")
    os.rename(source_filename, destination_filename)

# Rename a file
def rename_file():
    old_filename = input("Enter the name of the old file: ")
    new_filename = input("Enter the name of the new file: ")
    os.rename(old_filename, new_filename)

# Quit the program
def quit_program():
    sys.exit()

# Main loop
while True:
    #
