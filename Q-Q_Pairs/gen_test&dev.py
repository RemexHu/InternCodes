from tqdm import tqdm
import ujson as json
import random

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def gen_test(input_file, output_file=None, other_file=None):
    if not output_file:
        output_file = 'result_labeled'
    if not other_file:
        other_file = 'result_other'



    sampled_lines = []
    other_lines = []

    line_cnt = 0
    num_lines = get_number_of_lines(input_file)

    choice = random.sample(range(num_lines), 1000)

    query_count, candidate_count, selected_count, unselected_count = 0, 0, 0, 0

    invalid_chars = set(['。', '：', '-', '，'])
    with open(input_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines, ascii=True):
            try:
                sample = json.loads(line)
        #     sample is a dict
            except:
                continue
            line_cnt += 1

            documents = sample['documents']
            question = sample['question']
            query_count += 1
            title_list = {}

            if line_cnt in choice:
                for document in documents:
                    candidate_count += 1
                    title = document['title']
                    if document['is_selected']:
                        selected_count += 1
                        label = 1
                    else:
                        unselected_count += 1
                        label = 0
                    # label = document['most_related_para']
                    title_list[title] = label

                # print(title_list)
                if title_list:
                    for title, label in title_list.items():
                        sample_line = question + '\t' + title + '\t' + str(label) +'\n'
                        sampled_lines.append(sample_line)
            else:
                title_list = set()

                for document in documents:
                    if document['is_selected']:
                        title_list.add(document['title'])

                # print(title_list)
                if title_list:
                    for title in title_list:
                        sample_line = question + '\t' + title + '\n'
                        other_lines.append(sample_line)

    # print(query_count, candidate_count / query_count, selected_count / query_count, unselected_count / query_count)

    # print(len(sampled_lines))
    with open(output_file, "w", encoding='utf-8') as writer:
        writer.writelines(sampled_lines)
    with open(other_file, "w", encoding='utf-8') as writer:
        writer.writelines(other_lines)


gen_test('zhidao.dev.json')



