num_list = [1, 45, 30, 57, 65, 36, 25, 53, 21]

count = 0

for index, num in enumerate(num_list):
    if num == 36:
        count += 1

print("Total count of number 36:", count)