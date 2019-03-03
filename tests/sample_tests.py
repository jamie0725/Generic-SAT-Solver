import numpy as np
import os

from shutil import copy


def main():
    samples = 30
    np.random.seed(42)
    test_dir = os.path.abspath(os.path.dirname(__file__))
    dirnames = os.listdir('./')
    for dirname in dirnames:
        if 'samples' not in dirname and '.rar' not in dirname and '.py' not in dirname and '.txt' not in dirname:
            filenames = os.listdir(dirname)
            filenames = np.random.choice(filenames, samples, False)
            for file in filenames:
                src_file = os.path.join(test_dir, dirname, file)
                dest_dir = os.path.join(test_dir, 'samples', dirname)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                dest_file = os.path.join(dest_dir, file)
                copy(src_file, dest_file)


if __name__ == '__main__':
    main()
