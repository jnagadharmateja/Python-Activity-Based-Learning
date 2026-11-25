# Case 27: Advanced Numeric Pattern Generator

## Problem statement

Produce a symmetric numerical pattern for a user-specified dimension, validating invalid dimensions and aligning the output.

## Objectives

- Use nested loops to make a symmetric numeric diamond.
- Reject dimensions outside the chosen range.

## Assumptions

- Dimension is an integer from 1 to 9 and represents the largest number in the middle row.
- Each row ascends to its row number and descends to 1; leading spaces align the diamond.
- Numeric input must be entered in the requested format.

## Algorithm

1. Read and validate the dimension.
2. Visit the upper half including the middle row, then the lower half.
3. For each row, print leading spaces, ascending numbers and descending numbers.

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```text
READ n
IF n is outside 1 to 9: REPORT invalid
ELSE
  FOR line from 1 to 2*n-1
    FIND row number (increasing then decreasing)
    ADD leading spaces
    ADD numbers from 1 to row number
    ADD numbers from row number-1 down to 1
    PRINT line
```

## Python source code

[solution.py](solution.py)

## Test cases

1. **Diamond of size 3**

   Input (one value per line):

   ```text
3
   ```

   Expected: `    1 /   1 2 1 / 1 2 3 2 1 /   1 2 1 /     1`.

2. **Invalid dimension**

   Input (one value per line):

   ```text
0
   ```

   Expected: `Invalid dimension`.

3. **Minimum dimension**

   Input (one value per line):

   ```text
1
   ```

   Expected: `Dimension (1-9): 1 / `.

4. **Dimension too large**

   Input (one value per line):

   ```text
10
   ```

   Expected: `Invalid dimension`.

## Output screenshots

- Test 1: [output image](output-1.png) | [output text](output-1.txt)
- Test 2: [output image](output-2.png) | [output text](output-2.txt)
- Test 3: [output image](output-3.png) | [output text](output-3.txt)
- Test 4: [output image](output-4.png) | [output text](output-4.txt)

The images are made from actual captured program output; input is shown separately.

## Conclusion

The program solves this case using the rules and conditions stated above.
