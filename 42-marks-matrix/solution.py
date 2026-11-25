students = int(input("Number of students: "))
subjects = int(input("Number of subjects: "))
if students <= 0 or subjects <= 0:
    print("Invalid matrix dimensions.")
else:
    matrix = []
    valid = True
    for i in range(students):
        row = []
        for j in range(subjects):
            mark = float(input("S" + str(i + 1) + " subject " + str(j + 1) + ": "))
            if mark < 0 or mark > 100:
                valid = False
            row.append(mark)
        matrix.append(row)
    if not valid:
        print("Invalid mark: use 0 to 100.")
    else:
        totals = []
        for i in range(students):
            total = 0
            for mark in matrix[i]:
                total += mark
            totals.append(total)
            print("S" + str(i + 1), "total:", format(total, ".2f"), "average:", format(total / subjects, ".2f"))
        highest = max(totals)
        for i in range(students):
            if totals[i] == highest:
                print("Top performer: S" + str(i + 1))
        for j in range(subjects):
            total = 0
            for i in range(students):
                total += matrix[i][j]
            average = total / students
            if average < 40:
                status = "LOW"
            else:
                status = "OK"
            print("Subject", j + 1, "average:", format(average, ".2f"), status)
