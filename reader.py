from tqdm import tqdm
import ujson as json

num, cnt = 5, 0

Docs = []
Questions = []

with open('zhidao.dev.json.txt', 'r', encoding='utf-8') as reader:
    # for cnt in range(num):
    #     for line in reader:
    #         print(line)
    for line in tqdm(reader):
        line = line.strip()
        line_split = line.split('\t')

        doc = line_split[0]
        question = line_split[2]

        Docs.append(doc)
        Questions.append(question)

        # print(line_split)


with open('Q-Q_Pairs.txt', 'w', encoding='utf-8') as writer:
    for (doc, question) in zip(Docs, Questions):
        # print(doc)

        writer.write(doc + '\t' + question + '\n')


# print(Docs)
