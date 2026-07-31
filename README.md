# CS4306 Assignment 2: The Skyline Problem
 
## Team
 
- Jarren Shaw-Flores
- Nicholas Carrasquilla
- Alan Lopez
- Eduardo Arellano-Pacheco
## Overview
 
Computes the skyline of a set of rectangular buildings
using a divide-and-conquer algorithm, in **O(n log n)** time.
 
- `src/skyline.py` is the recursion driver (splits the building list, recurses,
  merges).
- `src/merge.py` combines two already-correct skylines into one.
- `src/io_utils.py` reads the comma-delimited input file, writes the
  comma-delimited output file.
- `tests/brute_force.py` is an independent O(n²) reference implementation
  used to cross-check the real algorithm's correctness, including a
  random stress test.
- `InputsOutputs/` — 5 required sample input/output pairs.
## How to run
 
```
python3 src/main.py <absolute_input_path> <absolute_output_path>
```
 
Example:
```
python3 src/main.py /home/you/project/InputsOutputs/Input1.txt /home/you/project/InputsOutputs/Output1.txt
```
 
 
### Input format
Comma-delimited, one building per line:
```
H1, Lx1, Rx1
H2, Lx2, Rx2
...
```
 
### Output format
Comma-delimited, one skyline strip per line:
```
h1, x1
h2, x2
...
```
 
## Running the tests
 
Runs all 5 `InputsOutputs/Input*.txt` files through `main.py` and checks
the output against the matching `Output*.txt`:
```
python3 tests/run_tests.py
```
 
Cross-checks the real algorithm against an independent brute-force
reference implementation, on both the saved test cases and 200 randomly
generated building sets:
```
python3 tests/brute_force.py
```