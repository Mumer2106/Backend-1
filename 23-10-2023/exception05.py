def divide_by(a,b):
    return a/b
try:
    ans = divide_by (40, 0)
except ZeroDivisionError as R:
    print(R, " ==> We cannot divide by zero")
