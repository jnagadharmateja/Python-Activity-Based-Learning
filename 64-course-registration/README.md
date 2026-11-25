# Case 64: Tuple-Based Course Registration Validation

**Student:** J NAGA DHARMA TEJA  
**Roll number:** 26000505

## Problem statement

Represent registrations as tuples, identify duplicate registrations and invalid course combinations, and determine students whose selections violate supplied rules.

## Objectives

- Store student-course pairs as tuples.
- Report duplicate registrations, disallowed combinations and affected students.

## Assumptions and rules

- Valid course codes are PY, DB, AI and ML. Student IDs must be nonempty.
- AI and ML cannot both be selected by the same student under this example rule.
- Matching is case-insensitive for IDs and codes. A repeated student-course pair is a duplicate; invalid records also make their nonempty student ID affected.
- Numeric prompts expect numeric input in the requested format; non-numeric input is outside these examples.

## Algorithm

1. Read the registrations as student ID and course code tuples.
2. Validate the ID and course, and detect previously seen pairs.
3. Build a list of student IDs and check each for the forbidden AI/ML combination.
4. Print each issue and the distinct affected student IDs, or report no issues.

## Flowchart

![Flowchart for Tuple-Based Course Registration Validation](flowchart.png)

The chart is a high-level view; validation and repeated processing are detailed in the algorithm and pseudocode.

## Pseudocode

```text
READ registrations into a list of tuples
FOR each tuple
  UNPACK student and course
  CHECK fields and duplicate pair
  RECORD affected student when possible
FOR each student
  IF both AI and ML exist: report combination
PRINT affected students or no issues
```

## Python source code

See [solution.py](solution.py). Run from this folder with `python solution.py` and enter the requested values.

## Test cases and output screenshots

### Test 1: Duplicate and forbidden combination

Input, one value per line:
```text
4
s1
AI
s1
ML
s1
AI
s2
PY
```
Expected checks: `Duplicate registration`; `Forbidden combination for S1`; `Affected students: S1`.

Actual output: [text](output-1.txt) | [output image](output-1.png).

### Test 2: Valid registrations

Input, one value per line:
```text
2
s1
PY
s2
ML
```
Expected checks: `No registration issues`.

Actual output: [text](output-2.txt) | [output image](output-2.png).

### Test 3: Invalid course

Input, one value per line:
```text
1
s3
XX
```
Expected checks: `Invalid registration`; `Affected students: S3`.

Actual output: [text](output-3.txt) | [output image](output-3.png).

The output images are rendered from the actual captured program runs; inputs are shown separately because piped input is not echoed by the program.

## Conclusion

This program demonstrates tuple-based course registration validation using the stated rules. The tests cover the main scenario and at least one additional or boundary condition. Different institutional rules can be substituted if required.
