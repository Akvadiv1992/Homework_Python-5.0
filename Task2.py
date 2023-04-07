a = int(input("Input A: "))
b = int(input("Input B: "))

def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)
print(sum(a, b))