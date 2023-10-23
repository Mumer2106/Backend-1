items = {1, 2, 3, 4, 5}

try:
    item = items[6]
except Exception as R:
    print(R, ":  An IndexError occurred")