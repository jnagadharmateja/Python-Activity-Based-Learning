key = input("Answer key (A-D): ").strip().upper()
count = int(input("Number of students: "))
valid_key = len(key) > 0
for ch in key:
    if ch not in "ABCD":
        valid_key = False
if not valid_key or count < 0:
    print("Invalid key or student count.")
else:
    for i in range(count):
        name = input("Student name: ").strip()
        answer = input("Answers (A-D or -): ").strip().upper()
        valid = len(name) > 0 and len(answer) == len(key)
        for ch in answer:
            if ch not in "ABCD-":
                valid = False
        if not valid:
            print("Invalid response for", name)
        else:
            correct = 0
            incorrect = 0
            unanswered = 0
            for j in range(len(key)):
                if answer[j] == "-":
                    unanswered += 1
                elif answer[j] == key[j]:
                    correct += 1
                else:
                    incorrect += 1
            score = correct * 4 - incorrect
            print(name, "Correct:", correct, "Incorrect:", incorrect,
                  "Unanswered:", unanswered, "Score:", score)
