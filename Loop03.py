row = int(input("Enter the number of row: "))

if row % 2 == 0:
    half = row // 2
else:
    half = row // 2 + 1
    
space = half - 1

for i in range(1, half + 1):
    print(" " * space + "*" *(2 * i - 1))
    space -= 1
space = 1
for i in range(half - 1, 0, -1):
    print(" " * space + "*" * (2 * i - 1))
    space += 1
    