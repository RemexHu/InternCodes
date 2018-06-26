from tqdm import tqdm
import ujson as json
import random

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def concat(input_file_1, input_file_2, output_file):

    num_lines_1 = get_number_of_lines(input_file_1)
    num_lines_2 = get_number_of_lines(input_file_2)

    sampled_lines_1 = []
    sampled_lines_2 = []


    with open(input_file_1, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines_1, ascii=True):

            sampled_lines_1.append(line)

    with open(input_file_2, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines_2, ascii=True):
            
            sampled_lines_2.append(line)

    with open(output_file, "w", encoding='utf-8') as writer:
        writer.writelines(sampled_lines_1)
        writer.writelines(sampled_lines_2)


concat('result_other.json', 'result_labeled.json', 'total.json')
print('cdcd')