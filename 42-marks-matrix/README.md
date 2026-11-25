# Case 42: Student Marks Matrix Analysis

## Problem statement

Analyse a matrix of student marks across subjects, calculate row-wise and column-wise statistics, identify top performers and detect subjects with low average performance.

## Objectives

- Calculate each student total and average.
- Calculate subject averages and identify all tied top performers and weak subjects.

## Assumptions

- Enter at least one student and one subject; marks are finite numbers from 0 to 100.
- Student labels are S1, S2, ... and subject labels are Subject 1, Subject 2, ....
- A subject is low performing when its class average is below 40. Top performers are students with the highest total, including ties.
- Numeric input must be entered in the requested format.

## Algorithm

1. Read matrix dimensions and student-wise marks, validating the range.
2. Compute and print each student total and average.
3. Find the maximum total and print all students with that total.
4. Compute every subject average and flag those below 40.

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```text
READ student and subject counts
READ matrix and validate every mark
FOR each student: calculate total and average
FIND maximum total and print all matching students
FOR each subject: calculate average
  IF average < 40: mark low
```

## Python source code

[solution.py](solution.py)

## Test cases

1. **Tied students and low subject**

   Input (one value per line):

   ```text
2
2
80
20
70
30
   ```

   Expected: `S1 total: 100.00 average: 50.00`; `Top performer: S1`; `Top performer: S2`; `Subject 2 average: 25.00 LOW`.

2. **Invalid mark**

   Input (one value per line):

   ```text
1
1
101
   ```

   Expected: `Invalid mark: use 0 to 100`.

3. **Non-finite mark**

   Input (one value per line):

   ```text
1
1
nan
   ```

   Expected: `Invalid mark: use 0 to 100`.

4. **Average at threshold**

   Input (one value per line):

   ```text
1
1
40
   ```

   Expected: `Subject 1 average: 40.00 OK`.

## Output screenshots

- Test 1: [output image](output-1.png) | [output text](output-1.txt)
- Test 2: [output image](output-2.png) | [output text](output-2.txt)
- Test 3: [output image](output-3.png) | [output text](output-3.txt)
- Test 4: [output image](output-4.png) | [output text](output-4.txt)

The images are made from actual captured program output; input is shown separately.

## Conclusion

The program solves this case using the rules and conditions stated above.
