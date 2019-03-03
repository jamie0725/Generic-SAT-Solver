import os


def main():
    filenames = os.listdir('./')
    dirname = os.path.dirname(__file__)
    rules = []
    with open('../sudoku-rules.txt', 'r') as rule_file:
        for line in rule_file:
            rules.append(line)

    for filename in filenames:
        output_count = 0

        if '.txt' in filename:
            file_dir = os.path.join(dirname, filename[:-4])
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            with open(filename, 'r') as file:
                for line in file:
                    outputs = []
                    outputs.append(rules[0])
                    index_cnt = 0
                    for char in line:
                        if char != '.' and char != '\n':
                            i = index_cnt // 9
                            j = index_cnt % 9
                            outputs.append('{}{}{}'.format(i + 1, j + 1, char) + ' 0\n')
                        index_cnt += 1
                    outputs.extend(rules[1:])
                    with open(file_dir + '/test_' + str(output_count) + '.txt', 'w+') as output_file:
                        output_file.writelines(outputs)
                    output_count += 1


if __name__ == '__main__':
    main()
