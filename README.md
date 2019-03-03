# Generic SAT solver

### About
This repository contains code for a generic SAT solver to solve SAT problems in the DIMACS format.

### Requirements
Python 3, numpy

### Running Instructions
For Windows:  
Run "SAT.bat -Sn input_file.txt" in command prompt.  
For Unix based systems:  
Run "sh SAT.sh -Sn input_file.txt" in the terminal.

### Description
The following heuristics are implemented:  
S1: Random Heuristic  
S2: Deterministic Two-Sided Jeroslow-Wang Heuristic  
S3: Probabilistic Two-Sided Jeroslow-Wang Heuristic  
S4: Deterministic DLIS Heuristic  
S5: Probabilistic DLIS Heuristic

### Additional Notes
For repeating our experiments mentioned in the report (if needed), please follow the following steps:
1. run translate_examples.py under tests/ to encode all test cases in DIMACS format.
2. run samples_tests.py under tests/ to sample test cases from different categories.
3. run run_experiments.py under the main folder to run the experiments.
