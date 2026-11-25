# Case 31: String-Based Examination Answer Evaluation

## Problem statement

Compare answer strings with an answer key, count correct, incorrect and unanswered responses, apply negative marking and show results.

## Objectives

- Evaluate multiple students against one key.
- Calculate the total using negative marks.

## Assumptions

- The key uses uppercase A, B, C or D only; responses use those letters or - for unanswered.
- Each correct answer gives 4 marks, each incorrect answer deducts 1, and unanswered answers give 0. Negative totals are allowed.
- A response must be the same length as the key. Input is converted to uppercase.
- Numeric input must be entered in the requested format.

## Algorithm

1. Read and validate the key and student count.
2. Read each name and answer string.
3. Check the length and permitted symbols.
4. Compare each answer with the key, count categories and print the score.

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```text
READ key and count
IF key or count is invalid: STOP
FOR each student
  READ name and response
  IF response invalid: REPORT and continue
  COUNT correct, incorrect and unanswered
  score = correct * 4 - incorrect
  PRINT counts and score
```

## Python source code

[solution.py](solution.py)

## Test cases

1. **Mixed answers and invalid record**

   Input (one value per line):

   ```text
ABCD
2
Ravi
AB-D
Anu
AXCD
   ```

   Expected: `Ravi Correct: 3 Incorrect: 0 Unanswered: 1 Score: 12`; `Invalid response for Anu`.

2. **Negative marks**

   Input (one value per line):

   ```text
AA
1
Kiran
BB
   ```

   Expected: `Correct: 0 Incorrect: 2 Unanswered: 0 Score: -2`.

3. **Unanswered and incorrect**

   Input (one value per line):

   ```text
ABC
1
Sita
A-B
   ```

   Expected: `Sita Correct: 1 Incorrect: 1 Unanswered: 1 Score: 3`.

## Output screenshots

- Test 1: [output image](output-1.png) | [output text](output-1.txt)
- Test 2: [output image](output-2.png) | [output text](output-2.txt)
- Test 3: [output image](output-3.png) | [output text](output-3.txt)

The images are made from actual captured program output; input is shown separately.

## Conclusion

The program solves this case using the rules and conditions stated above.
