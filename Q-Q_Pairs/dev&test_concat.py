from tqdm import tqdm
import ujson as json
import random

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def test_cleaning(text_file, label_file, output_file):

    line_cnt = 0
    result_lines = []
    num_lines = get_number_of_lines(text_file)

    with open(text_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines, ascii=True):
            result_lines.append(line.strip())

    with open(label_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines, ascii=True):
            result_lines[line_cnt] = result_lines[line_cnt] + '\t' + line
            line_cnt += 1



    with open(output_file, "w", encoding='utf-8') as writer:
        writer.writelines(result_lines)


test_cleaning('queries_tst.txt', 'labels_tst.txt', 'tst.clean.txt')