def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()

        print(file_contents)

        return file_contents
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None

file_name = "example.txt"
contents = read_file(file_name)
if contents is not None:
    pass
