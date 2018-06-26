from tqdm import tqdm
import ujson as json

def get_number_of_lines(file_path):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def gen_test(input_file, output_file=None):
    if not output_file:
        output_file = 'result_labeled.txt'

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
            title_list = {}

            for document in documents:
                title = document['title']
                if document['is_selected']:
                    label = 1
                else:
                    label = 0
                # label = document['most_related_para']
                title_list[title] = label

            # print(title_list)
            if title_list:
                for title, label in title_list.items():
                    sample_line = question + '\t' + title + '\t' + str(label) +'\n'
                    sampled_lines.append(sample_line)

    # print(len(sampled_lines))
    with open(output_file, "w", encoding='utf-8') as writer:
        writer.writelines(sampled_lines)


gen_test('zhidao.dev.json')



