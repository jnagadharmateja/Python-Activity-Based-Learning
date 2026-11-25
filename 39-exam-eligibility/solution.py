attendance = float(input("Attendance percentage: "))
lab = input("Lab completed (Y/N): ").strip().upper()
marks = float(input("Internal marks out of 40: "))
fees = input("Fees cleared (Y/N): ").strip().upper()
if attendance < 0 or attendance > 100 or marks < 0 or marks > 40 or lab not in ("Y", "N") or fees not in ("Y", "N"):
    print("Invalid input values.")
else:
    reasons = []
    if attendance < 75:
        reasons.append("Attendance below 75 percent")
    if lab != "Y":
        reasons.append("Laboratory not completed")
    if marks < 16:
        reasons.append("Internal marks below 16")
    if fees != "Y":
        reasons.append("Fees not cleared")
    if len(reasons) == 0:
        print("Eligible for final examination")
    else:
        print("Not eligible:")
        for reason in reasons:
            print("-", reason)
