a = int(input("Input A: "))
b = int(input("Input B: "))

def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b - 1)
print(a,"в степени",b, end=' = ')
print(degree(a, b))