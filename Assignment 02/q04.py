def read_even_numbered_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        even_lines = [line for index, line in enumerate(lines) if index % 2 == 1]

        return even_lines
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None

file_name = "example.txt"
even_lines = read_even_numbered_lines(file_name)
if even_lines is not None:
    pass
