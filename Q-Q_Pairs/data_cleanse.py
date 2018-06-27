from tqdm import tqdm
import re

def cleanse(input_file, output_file):
    tails = set()


    with open(input_file, 'r', encoding='utf-8') as reader:
        for line in tqdm(reader):

            split_line = line.split('\t')
            tail = split_line[-1]

            split_tail = re.split('-|_', tail)
            if len(split_tail) > 1:
                print(split_tail[-1])



cleanse('result_other', '')