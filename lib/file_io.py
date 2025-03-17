# lib/file_io.py

def write_file(file_name, file_content):
    """
    Write content to a new text file.
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, file_content):
    """
    Append content to an existing text file.
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(file_content)  # Removed the \n before file_content

def read_file(file_name):
    """
    Read and return content from a text file.
    """
    with open(f"{file_name}.txt", "r") as file:
        return file.read()