from tqdm import tqdm
import ujson as json
import random

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def dump(input_file, output_file=None):
    if not output_file:
        output_file = 'result_aug.txt'

    sampled_cnt = 10
    sampled_lines = []

    line_cnt = 0
    num_lines = get_number_of_lines(input_file)

    invalid_chars = set(['。', '：', '-', '，'])
    with open(input_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines, ascii=True):
            try:
                sample = json.loads(line)
        #     sample is a dict
            except:
                continue


            documents = sample['documents']
            question = sample['question']
            title_set = set()

            for document in documents:
                if document['is_selected']:
                    title_set.add(document['title'])

            title_list = list(title_set)

            if title_set:
                for title in title_set:
                    sample_line = question + '\t' + title +'\n'
                    sampled_lines.append(sample_line)

            for i in range(len(title_list) - 1):
                for j in range(i + 1, len(title_list)):
                    sample_line = title_list[i] + '\t' + title_list[j] + '\n'
                    sampled_lines.append(sample_line)

    with open(output_file, "w", encoding='utf-8') as writer:
        writer.writelines(sampled_lines)




dump('zhidao.dev.json')
