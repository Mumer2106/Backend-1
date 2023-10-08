num_list = [1, 55, 30, 47, 60, 36, 25, 80]

count = 0

for index, num in enumerate(num_list):
    if num == 36:
        print("Number found at position:", index)
        count += 1

print("Total count of number 36:", count)