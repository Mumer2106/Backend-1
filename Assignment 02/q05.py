def read_file_in_reverse(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            reversed_lines = list(reversed(lines))

        for line in reversed_lines:
            print(line.strip())

        return reversed_lines
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None

file_name = "example.txt"
reversed_lines = read_file_in_reverse(file_name)
if reversed_lines is not None:
    pass
