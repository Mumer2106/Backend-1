def read_file_into_list(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        return lines
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None

file_name = "example.txt"
lines = read_file_into_list(file_name)
if lines is not None:
    pass