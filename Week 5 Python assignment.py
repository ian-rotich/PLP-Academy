# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("12345\n")
    file.write("Line 3 with a mix of strings and numbers.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to open the file.")
finally:
    print("File reading complete.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1.\n")
        file.write("67890\n")
        file.write("Another line with appended text.\n")
    print("Three lines appended to my_file.txt.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to open the file.")
finally:
    print("File appending complete.")
