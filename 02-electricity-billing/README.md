# Case 2: Progressive Electricity Billing

## Problem statement

Calculate household bills with consumption slabs, fixed charges, surcharges and rebates. Compare monthly bills and identify unusual increases.

## Objectives

- Calculate a progressive bill for each month.
- Compare consecutive bills and report unusually large increases.

## Assumptions

- Monthly units must be non-negative whole numbers.
- First 100 units cost Rs 3 each, next 100 Rs 5 each and units above 200 Rs 7 each.
- Fixed charge is Rs 50. Add 10% of energy charge as surcharge if units exceed 300. Give a Rs 20 rebate if units are at most 100.
- An increase over 25% from the previous bill is unusual; equality is not unusual. All amounts are in rupees.
- Numeric input must be entered in the requested format.

## Algorithm

1. Read the number of months and the units for each month. Stop if units are negative.
2. Calculate the energy charge progressively for each month.
3. Add the fixed charge and applicable surcharge, then subtract the rebate.
4. Print each bill and compare it with the preceding month.

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```text
READ number of months
FOR each month
  READ units
  IF units < 0: PRINT error and STOP
  CALCULATE energy charge using slabs
  ADD fixed charge and any surcharge
  SUBTRACT applicable rebate
  IF previous bill exists AND current > previous * 1.25
    REPORT unusual increase
  PRINT bill
END FOR
```

## Python source code

[solution.py](solution.py)

## Test cases

1. **Slabs, rebate and increase**

   Input (one value per line):

   ```text
3
100
200
301
   ```

   Expected: `Month 1 bill: Rs 330.00`; `Month 2 bill: Rs 850.00`; `Month 3 bill: Rs 1707.70`; `Unusual increase`.

2. **Invalid units**

   Input (one value per line):

   ```text
1
-2
   ```

   Expected: `Units cannot be negative`.

3. **Increase at exactly 25 percent**

   Input (one value per line):

   ```text
2
10
15
   ```

   Expected: `Month 1 bill: Rs 60.00`; `Month 2 bill: Rs 75.00`; `No unusual increase`.

4. **Surcharge boundary**

   Input (one value per line):

   ```text
2
300
301
   ```

   Expected: `Month 1 bill: Rs 1550.00`; `Month 2 bill: Rs 1707.70`; `No unusual increase`.

## Output screenshots

- Test 1: [output image](output-1.png) | [output text](output-1.txt)
- Test 2: [output image](output-2.png) | [output text](output-2.txt)
- Test 3: [output image](output-3.png) | [output text](output-3.txt)
- Test 4: [output image](output-4.png) | [output text](output-4.txt)

The images are made from actual captured program output; input is shown separately.

## Conclusion

The program solves this case using the rules and conditions stated above.
