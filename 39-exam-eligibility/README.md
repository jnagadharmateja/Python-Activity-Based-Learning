# Case 39: Multi-Stage Examination Eligibility System

**Student:** J NAGA DHARMA TEJA  
**Roll number:** 26000505

## Problem statement

Determine final examination eligibility using attendance, laboratory completion, internal assessment and fee clearance, reporting every unmet requirement.

## Objectives

- Evaluate all four requirements.
- List each unmet condition instead of stopping at the first.

## Assumptions and rules

- Attendance must be between 0 and 100 and at least 75%.
- Laboratory completion and fee clearance must be Y or N. Internal marks must be from 0 to 40, with at least 16 required.
- All four conditions must be met. Invalid input values are reported separately from an eligibility decision.
- Numeric prompts expect numeric input in the requested format; non-numeric input is outside these examples.

## Algorithm

1. Read attendance, laboratory status, internal marks and fee status.
2. Validate the input ranges and Y/N choices.
3. Check each requirement independently and collect all reasons.
4. Print eligible if no requirement is missing, otherwise print all reasons.

## Flowchart

![Flowchart for Multi-Stage Examination Eligibility System](flowchart.png)

The chart is a high-level view; validation and repeated processing are detailed in the algorithm and pseudocode.

## Pseudocode

```text
READ attendance, lab status, internal marks, fee status
IF values are invalid: report invalid
ELSE
  CHECK each requirement and record failures
  IF no failures: report eligible
  ELSE: report every failure
```

## Python source code

See [solution.py](solution.py). Run from this folder with `python solution.py` and enter the requested values.

## Test cases and output screenshots

### Test 1: All conditions met at boundary

Input, one value per line:
```text
75
Y
16
Y
```
Expected checks: `Eligible for final examination`.

Actual output: [text](output-1.txt) | [output image](output-1.png).

### Test 2: All conditions fail

Input, one value per line:
```text
74
N
15
N
```
Expected checks: `Not eligible`; `Attendance below`; `Laboratory not completed`; `Internal marks below`; `Fees not cleared`.

Actual output: [text](output-2.txt) | [output image](output-2.png).

### Test 3: Invalid range

Input, one value per line:
```text
101
Y
20
Y
```
Expected checks: `Invalid input values`.

Actual output: [text](output-3.txt) | [output image](output-3.png).

The output images are rendered from the actual captured program runs; inputs are shown separately because piped input is not echoed by the program.

## Conclusion

This program demonstrates multi-stage examination eligibility system using the stated rules. The tests cover the main scenario and at least one additional or boundary condition. Different institutional rules can be substituted if required.
