'''
Implement a program that takes user input for a filename, opens the file in read
mode, and displays its contents. Handle the FileNotFoundError and display an error
message if the file is not found.

'''


def read_file_check(filename: str) -> None:
    """
    Read and display the contents of the file.

    Args:
        filename (str): The name of the file to be read.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Take user input for the filename
filename = input("Enter the name of the file: ")


read_file_check(filename)
