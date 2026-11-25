count = int(input("Number of registrations: "))
if count < 0:
    print("Invalid registration count.")
else:
    records = []
    affected = []
    students = []
    issues = 0
    for i in range(count):
        student = input("Student ID: ").strip().upper()
        course = input("Course code: ").strip().upper()
        record = (student, course)
        if student != "" and student not in students:
            students.append(student)
        if student == "" or course not in ("PY", "DB", "AI", "ML"):
            print("Invalid registration:", record)
            issues += 1
            if student != "" and student not in affected:
                affected.append(student)
        if record in records:
            print("Duplicate registration:", record)
            issues += 1
            if student != "" and student not in affected:
                affected.append(student)
        records.append(record)
    for student in students:
        has_ai = False
        has_ml = False
        for record in records:
            sid, course = record
            if sid == student and course == "AI":
                has_ai = True
            if sid == student and course == "ML":
                has_ml = True
        if has_ai and has_ml:
            print("Forbidden combination for", student, ": AI and ML")
            issues += 1
            if student not in affected:
                affected.append(student)
    if issues == 0:
        print("No registration issues")
    elif len(affected) == 0:
        print("No identifiable affected student")
    else:
        print("Affected students:", ", ".join(affected))
