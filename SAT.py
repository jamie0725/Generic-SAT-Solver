#!/usr/bin/python
# # SAT solver script

import sys
from utils import DP


def main(argv):
    if argv[0] == '-S1':
        print('The splitting strategy you choose is: Random Split Heuristic.')
        sat_solver = DP(argv[1])
        sat_solver.split = 1
    elif argv[0] == '-S2':
        print('The splitting strategy you choose is: (Deterministic) Jeroslow-Wang Heuristic.')
        sat_solver = DP(argv[1])
        sat_solver.split = 2
    elif argv[0] == '-S3':
        print('The splitting strategy you choose is: Probabilistic Jeroslow-Wang Heuristic.')
        sat_solver = DP(argv[1])
        sat_solver.split = 3
    elif argv[0] == '-S4':
        print('The splitting strategy you choose is: (Deterministic) DLIS Heuristic.')
        sat_solver = DP(argv[1])
        sat_solver.split = 4
    elif argv[0] == '-S5':
        print('The splitting strategy you choose is: Probabilistic DLIS Heuristic.')
        sat_solver = DP(argv[1])
        sat_solver.split = 5
    else:
        print('Incorrect input: your input command should be strictly of the following format:')
        print('--------------------')
        print("for Linux: 'sh SAT.sh -Sn inputfile'")
        print("for Windows: 'SAT.bat -Sn inputfile'")
        print('--------------------')
        print("Note: n can be 1 ~ 5, which corresponds to 5 different splitting heuristics.")
        exit()
    print('--------------------')
    print('Processing...')
    print('--------------------')
    clauses = sat_solver.read()
    clauses = sat_solver.tautology(clauses)
    var = sat_solver.solver(clauses)
    print('Done!')
    print('--------------------')
    if var is False:
        print('Oops, the problem is not solvable...')
        sat_solver.output_results()
    else:
        sat_solver.output_results(var)


if __name__ == '__main__':
    main(sys.argv[1:])
