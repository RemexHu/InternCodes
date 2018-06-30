import random


lines = open('result.txt').read().splitlines()
select_lines = []

for _ in range(10):
    myline = random.choice(lines)
    select_lines.append(myline + '\n')

with open('select.txt', 'w', encoding='utf-8') as writer:
    writer.writelines(select_lines)
