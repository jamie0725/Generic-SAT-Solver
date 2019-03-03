import csv
import os
import numpy as np
from utils import DP


def main():
    base_dirname = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tests', 'samples')
    dirnames = [f.path for f in os.scandir(base_dirname) if f.is_dir()]

    samples = 30
    reps = 30
    testcases = samples * len(dirnames)

    # Choose strategy. (1 - 5)
    s = 5

    if s == 2 or s == 4:
        repetition = 1
        rows = 1
    else:
        repetition = reps
        rows = reps

    with open('./experiment_s{}.csv'.format(s), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

    statistics = np.empty((rows, testcases), dtype=np.float)

    i = 0
    print('Strategy {}:'.format(s))
    for i_r in np.arange(repetition):
        print('Repetition: {}'.format(i_r + 1))
        with open('./experiment_s{}.csv'.format(s), 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Repetition: {}'.format(i_r + 1)])
        j = 0
        for dirname in dirnames:
            filenames = os.listdir(dirname)
            for file in filenames:
                file = os.path.join(base_dirname, dirname, file)
                print('Processing: ' + file)
                sat_solver = DP(file)
                sat_solver.split = s

                clauses = sat_solver.read()
                clauses = sat_solver.tautology(clauses)
                var = sat_solver.solver(clauses)
                statistics[i, j] = sat_solver.count
                j += 1

        with open('./experiment_s{}.csv'.format(s), 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(statistics[i, :].tolist())

        i += 1


if __name__ == '__main__':
    main()
