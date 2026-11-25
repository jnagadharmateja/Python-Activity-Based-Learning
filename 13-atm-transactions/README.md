# Case 13: ATM Transaction Sequence Simulation

**Student:** J NAGA DHARMA TEJA  
**Roll number:** 26000505

## Problem statement

Process deposits and withdrawals, maintain a simulated balance, enforce withdrawal limits, reject invalid transactions and produce a summary.

## Objectives

- Update a balance for a sequence of transactions.
- Reject invalid transactions and show totals.

## Assumptions and rules

- Opening balance is Rs 1,000.
- Amounts must be positive numbers; the withdrawal limit is Rs 5,000 per transaction and withdrawal cannot exceed the balance.
- Transaction type is D for deposit or W for withdrawal, without regard to case. Rejected operations do not change the balance.
- Numeric prompts expect numeric input in the requested format; non-numeric input is outside these examples.

## Algorithm

1. Start with the opening balance and zero totals.
2. Read each type and amount.
3. Check type, amount, balance and withdrawal limit.
4. Apply valid transactions, count rejections and print the summary.

## Flowchart

![Flowchart for ATM Transaction Sequence Simulation](flowchart.png)

The chart is a high-level view; validation and repeated processing are detailed in the algorithm and pseudocode.

## Pseudocode

```text
SET balance to 1000
READ number of transactions
FOR every transaction
  READ type and amount
  IF valid deposit: add to balance and deposit total
  ELSE IF valid withdrawal: subtract and add to withdrawal total
  ELSE: count rejection
  PRINT result
PRINT balance, totals and rejection count
```

## Python source code

See [solution.py](solution.py). Run from this folder with `python solution.py` and enter the requested values.

## Test cases and output screenshots

### Test 1: Valid and rejected transactions

Input, one value per line:
```text
3
D
500
W
1200
W
400
```
Expected checks: `Deposits: Rs 500.00`; `Withdrawals: Rs 1200.00`; `Rejected: 1`; `Balance: Rs 300.00`.

Actual output: [text](output-1.txt) | [output image](output-1.png).

### Test 2: Limit and invalid amount

Input, one value per line:
```text
2
W
6000
D
0
```
Expected checks: `Rejected: 2`; `Balance: Rs 1000.00`.

Actual output: [text](output-2.txt) | [output image](output-2.png).

The output images are rendered from the actual captured program runs; inputs are shown separately because piped input is not echoed by the program.

## Conclusion

This program demonstrates atm transaction sequence simulation using the stated rules. The tests cover the main scenario and at least one additional or boundary condition. Different institutional rules can be substituted if required.
