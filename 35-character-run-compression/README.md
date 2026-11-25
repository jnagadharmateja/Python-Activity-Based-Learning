# Case 35: Text Compression Using Character Runs

**Student:** J NAGA DHARMA TEJA  
**Roll number:** 26000505

## Problem statement

Encode a string by grouping consecutive repeated characters and compare the original and encoded lengths, including cases where encoding is not beneficial.

## Objectives

- Group consecutive identical characters.
- Compare the encoded and original lengths.

## Assumptions and rules

- Runs are encoded as character followed by its decimal count, for example AAABB becomes A3B2.
- Counts are included even for a single character; spaces and digits are counted as characters too.
- The output is for size comparison only: the simple format is ambiguous for decoding input containing digits. Empty input is allowed.
- Numeric prompts expect numeric input in the requested format; non-numeric input is outside these examples.

## Algorithm

1. Read the text.
2. Traverse the text while counting each consecutive character run.
3. Append each character and its count to the encoded string.
4. Compare lengths and say whether encoding saves space.

## Flowchart

![Flowchart for Text Compression Using Character Runs](flowchart.png)

The chart is a high-level view; validation and repeated processing are detailed in the algorithm and pseudocode.

## Pseudocode

```text
READ text
SET encoded to empty
WHILE characters remain
  COUNT identical consecutive characters
  APPEND character and count
PRINT encoded and both lengths
IF encoded length < original length: report saving
ELSE: report not beneficial
```

## Python source code

See [solution.py](solution.py). Run from this folder with `python solution.py` and enter the requested values.

## Test cases and output screenshots

### Test 1: Repeated characters

Input, one value per line:
```text
AAAABBBCC
```
Expected checks: `Encoded: A4B3C2`; `Original length: 9`; `Encoded length: 6`; `Compression is beneficial`.

Actual output: [text](output-1.txt) | [output image](output-1.png).

### Test 2: Non-repeating characters

Input, one value per line:
```text
ABC
```
Expected checks: `Encoded: A1B1C1`; `Original length: 3`; `Encoded length: 6`; `Compression is not beneficial`.

Actual output: [text](output-2.txt) | [output image](output-2.png).

### Test 3: Empty text

Input, one value per line:
```text
(empty line)
```
Expected checks: `Original length: 0`; `Encoded length: 0`; `Compression is not beneficial`.

Actual output: [text](output-3.txt) | [output image](output-3.png).

The output images are rendered from the actual captured program runs; inputs are shown separately because piped input is not echoed by the program.

## Conclusion

This program demonstrates text compression using character runs using the stated rules. The tests cover the main scenario and at least one additional or boundary condition. Different institutional rules can be substituted if required.
