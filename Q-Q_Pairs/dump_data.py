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


def dump(input_file, output_file=None):
    if not output_file:
        output_file = input_file + '.txt'

    sampled_cnt = 100
    sampled_lines = []
    
    line_cnt = 0
    num_lines = get_number_of_lines(input_file)

    invalid_chars = set(['。', '：', '-', '，'])
    with open(input_file, "r", encoding='utf-8') as reader:
        for line in tqdm(reader, total=num_lines, ascii=True):
            try:
                sample = json.loads(line)
            except:
                continue
            
            question_type = sample['question_type']
            fact_or_opinion = sample['fact_or_opinion']
            answer_docs = sample['answer_docs']
            documents = sample['documents']

            for i, answer_doc in enumerate(answer_docs):
                if answer_doc < 0 or answer_doc >= len(documents):
                    continue
                
                document = documents[answer_doc]
                most_related_para = document['most_related_para']
                title_tokens = document['segmented_title']
                context_tokens = document['segmented_paragraphs'][most_related_para]
                doc_tokens = title_tokens + context_tokens
                len_title_tokens = len(title_tokens)
                answer_span = sample['answer_spans'][i]
                y1, y2 = answer_span[0], answer_span[-1]
                y1 += len_title_tokens
                y2 += len_title_tokens

                len_answer_tokens = y2 - y1 + 1
                len_doc_tokens = len(doc_tokens)
                if len_answer_tokens >= len_doc_tokens:
                    continue

                if y1 < 0 or y1 >= len_doc_tokens:
                    continue

                first_answer_token = doc_tokens[y1]
                ques_tokens = sample["segmented_question"]
                len_ques_tokens = len(ques_tokens)

                if len_doc_tokens > 400 or len_ques_tokens > 50 or len_answer_tokens > 100 or first_answer_token in invalid_chars:
                    continue
                
                line_cnt += 1
                sample_insert_index = -1
                if line_cnt <= sampled_cnt:
                    sample_insert_index = line_cnt - 1
                    sampled_lines.append('')
                else:
                    random_index = random.randint(0, line_cnt - 1)
                    if random_index < sampled_cnt:
                        sample_insert_index = random_index

                if sample_insert_index != -1:
                    doc = ''.join(doc_tokens).replace('\n', ' ')
                    question = ''.join(ques_tokens).replace('\n', ' ')
                    answer = [''.join(doc_tokens[y1:y2+1]).replace('\n', ' ')]
                    line = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(doc, len_doc_tokens, question, len_ques_tokens, answer, len_answer_tokens, question_type, fact_or_opinion)
                    sampled_lines[sample_insert_index] = line
    
    print('Total valid records: {}'.format(line_cnt))
    with open(output_file, "w", encoding='utf-8') as writer:
        writer.write('Document\tDocLen\tQuestion\tQuesLen\tAnswer\tAnsLen\tType\tFactOpinion\n')
        writer.writelines(sampled_lines)

dump('zhidao.dev.json')
