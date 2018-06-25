from tqdm import tqdm
import ujson as json
import random

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    print(count)
    return count


def delete(input_file, output_file=None):
    if not output_file:
        output_file = 'scratch.txt'

    num_lines = get_number_of_lines(input_file)
    lines = []
    with open(input_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=10, ascii=True):
            lines.append(line)
            if len(lines) > 10:
                break

    with open(output_file, "w", encoding='utf-8') as writer:
        writer.writelines(lines)



delete('zhidao.dev.json')
