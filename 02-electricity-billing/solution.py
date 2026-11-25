months = int(input("Number of months: "))
if months <= 0:
    print("Enter at least one month.")
else:
    bills = []
    for month in range(1, months + 1):
        units = int(input("Units for month " + str(month) + ": "))
        if units < 0:
            print("Units cannot be negative. Stopping.")
            break
        if units <= 100:
            energy = units * 3
        elif units <= 200:
            energy = 100 * 3 + (units - 100) * 5
        else:
            energy = 100 * 3 + 100 * 5 + (units - 200) * 7
        surcharge = energy * 0.10 if units > 300 else 0
        rebate = 20 if units <= 100 else 0
        bill = energy + 50 + surcharge - rebate
        bills.append(bill)
        print("Month", month, "bill: Rs", format(bill, ".2f"))
        if len(bills) > 1:
            if bills[-1] > bills[-2] * 1.25:
                print("Unusual increase from previous month")
            else:
                print("No unusual increase")
