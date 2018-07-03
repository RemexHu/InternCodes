from tqdm import tqdm
import ujson as json
import random

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def test_splitting(input_file, output_queries=None, output_label=None):


    label_lines = []
    result_lines = []

    line_cnt = 0
    num_lines = get_number_of_lines(input_file)

    with open(input_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines, ascii=True):
            split_line = line.split('\t')
            result_lines.append(split_line[0] + '\t' + split_line[1] + '\n')
            label_lines.append(split_line[-1])


    with open(output_queries, 'w', encoding='utf-8') as writer:
        writer.writelines(result_lines)

    with open(output_label, 'w', encoding='utf-8') as writer:
        writer.writelines(label_lines)



test_splitting('result_tst.json', 'queries_tst.txt', 'labels_tst.txt')
