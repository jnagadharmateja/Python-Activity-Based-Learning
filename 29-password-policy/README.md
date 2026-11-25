# Case 29: Password Policy Validation Engine

## Problem statement

Evaluate password strings against minimum length, character categories, repetition and prohibited substrings, and explain every failed condition.

## Objectives

- Check each password against a stated policy.
- Print all reasons a password fails.

## Assumptions

- Minimum length is 8 characters. At least one ASCII uppercase letter, lowercase letter, digit and one of !@#$% is required.
- Three identical consecutive characters are not allowed. The substrings password and admin are prohibited regardless of case.
- This is a classroom policy checker, not a secure password storage system.

## Algorithm

1. Read a password.
2. Check its length and character categories using string membership and a loop.
3. Check consecutive repeated characters and prohibited substrings.
4. Print all failures or print that it is valid.

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```text
READ password
CHECK length and four character categories
CHECK any three consecutive equal characters
CHECK prohibited substrings ignoring case
IF no failures: PRINT valid
ELSE: PRINT each failure
```

## Python source code

[solution.py](solution.py)

## Test cases

1. **Valid password**

   Input (one value per line):

   ```text
Abc123!x
   ```

   Expected: `Valid password`.

2. **Multiple failures**

   Input (one value per line):

   ```text
passwordaaa
   ```

   Expected: `Invalid password`; `Uppercase letter required`; `Digit required`; `Special character`; `Three identical`; `Prohibited substring`.

3. **Prohibited admin substring**

   Input (one value per line):

   ```text
Admin12!x
   ```

   Expected: `Invalid password`; `Prohibited substring: admin`.

## Output screenshots

- Test 1: [output image](output-1.png) | [output text](output-1.txt)
- Test 2: [output image](output-2.png) | [output text](output-2.txt)
- Test 3: [output image](output-3.png) | [output text](output-3.txt)

The images are made from actual captured program output; input is shown separately.

## Conclusion

The program solves this case using the rules and conditions stated above.
