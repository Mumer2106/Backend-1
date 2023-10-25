def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n', 1)[0]

    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(first_line)

    except FileNotFoundError:
        print(f"Output file not found: {output_filename}")


file_contents = "This is the first line.\nThis is the second line.\nThis is the third line."
output_filename = "output.txt"
write_first_line_to_file(file_contents, output_filename)
