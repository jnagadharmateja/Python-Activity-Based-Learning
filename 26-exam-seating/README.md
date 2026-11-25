# Case 26: Nested Loop Examination Seating Generator

**Student:** J NAGA DHARMA TEJA  
**Roll number:** 26000505

## Problem statement

Generate an examination seating arrangement using row and column identifiers, reserved positions, alternate seating restrictions and fixed classroom capacity.

## Objectives

- Generate a row-by-column seating plan.
- Respect reserved positions and alternating-seat rules.

## Assumptions and rules

- A classroom has a maximum of 5 rows and 6 columns.
- Rows and columns are numbered from 1. The seat at row 1, column 1 is reserved.
- Only positions with an even row-plus-column sum are allowed for students; the reserved position takes priority.
- Students are assigned sequential identifiers S01, S02 and so on. Extra students remain unseated.
- Numeric prompts expect numeric input in the requested format; non-numeric input is outside these examples.

## Algorithm

1. Read rows, columns and student count and validate limits.
2. Use nested loops to visit every seat.
3. Mark the reserved seat first, then block alternating seats, then assign available students.
4. Print the arrangement and number of students still unseated.

## Flowchart

![Flowchart for Nested Loop Examination Seating Generator](flowchart.png)

The chart is a high-level view; validation and repeated processing are detailed in the algorithm and pseudocode.

## Pseudocode

```text
READ rows, columns, students
IF dimensions or student count are invalid: STOP
FOR each row
  FOR each column
    IF reserved position: mark RES
    ELSE IF row + column is odd: mark X
    ELSE IF students remain: assign next student
    ELSE: mark EMPTY
  PRINT row
PRINT unseated count
```

## Python source code

See [solution.py](solution.py). Run from this folder with `python solution.py` and enter the requested values.

## Test cases and output screenshots

### Test 1: More students than available seats

Input, one value per line:
```text
2
3
4
```
Expected checks: `R1C1:RES  R1C2:X  R1C3:S01`; `R2C1:X  R2C2:S02  R2C3:X`; `Unseated: 2`.

Actual output: [text](output-1.txt) | [output image](output-1.png).

### Test 2: Invalid room size

Input, one value per line:
```text
6
2
3
```
Expected checks: `Invalid dimensions`.

Actual output: [text](output-2.txt) | [output image](output-2.png).

The output images are rendered from the actual captured program runs; inputs are shown separately because piped input is not echoed by the program.

## Conclusion

This program demonstrates nested loop examination seating generator using the stated rules. The tests cover the main scenario and at least one additional or boundary condition. Different institutional rules can be substituted if required.
