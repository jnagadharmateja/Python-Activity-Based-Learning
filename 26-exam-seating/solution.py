rows = int(input("Rows (1-5): "))
cols = int(input("Columns (1-6): "))
students = int(input("Number of students: "))
if rows < 1 or rows > 5 or cols < 1 or cols > 6 or students < 0:
    print("Invalid dimensions or student count.")
else:
    assigned = 0
    for row in range(1, rows + 1):
        line = []
        for col in range(1, cols + 1):
            if row == 1 and col == 1:
                seat = "RES"
            elif (row + col) % 2 != 0:
                seat = "X"
            elif assigned < students:
                assigned += 1
                seat = "S" + str(assigned).zfill(2)
            else:
                seat = "EMPTY"
            line.append("R" + str(row) + "C" + str(col) + ":" + seat)
        print("  ".join(line))
    print("Assigned:", assigned)
    print("Unseated:", students - assigned)
