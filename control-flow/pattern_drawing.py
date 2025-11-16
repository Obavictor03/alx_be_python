size = int(input("Enter the size of the pattern:"))

count = 0

while count < size:
    for i in range(size):
        print("*", end="")
    count += 1
    print()