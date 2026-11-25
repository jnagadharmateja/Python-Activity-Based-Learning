n = int(input("Dimension (1-9): "))
if n < 1 or n > 9:
    print("Invalid dimension.")
else:
    for line in range(1, 2 * n):
        if line <= n:
            row = line
        else:
            row = 2 * n - line
        output = "  " * (n - row)
        for number in range(1, row + 1):
            output += str(number) + " "
        for number in range(row - 1, 0, -1):
            output += str(number) + " "
        print(output.rstrip())
