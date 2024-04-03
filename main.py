def write_to_file():
    try:
        # Create and write to the file
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Another line here with special characters: @#$%\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Write operation completed.")

def read_and_display():
    try:
        # Read and display the contents of the file
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Read operation completed.")

def append_to_file():
    try:
        # Append to the file
        with open("my_file.txt", "a") as file:
            file.write("Appending a new line.\n")
            file.write("67890\n")
            file.write("One more line added for good measure.\n")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    finally:
        print("Append operation completed.")

# Main function
def main():
    # Write to file
    write_to_file()

    # Read and display file contents
    read_and_display()

    # Append to file
    append_to_file()

    # Read and display updated contents
    read_and_display()

if __name__ == "__main__":
    main()
