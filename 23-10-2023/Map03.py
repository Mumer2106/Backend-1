Number= {1,2,3,4,5,6}
def find_num(Number):
    return Number*2

map_Number= map(find_num, Number)
print(map_Number)
for x in map_Number:
    print(x)