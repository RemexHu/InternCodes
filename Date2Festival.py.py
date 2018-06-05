# This code is running on windows desktop

file = open('C://Users//t-ruhu//Downloads//FESTIVAL.txt', mode='r', encoding="utf8")
example = open('C://Users//t-ruhu//Downloads//data_3500k_label.txt', mode='r', encoding="utf8")
result = open('C://Users//t-ruhu//Downloads//result.txt', mode='w', encoding="utf8")

lines = file.readlines()

festival_dict = set()

for line in lines:
    # print(line)
    fest = line.replace(' FESTIVAL', '')
    fest = fest.strip()
    festival_dict.add(fest)

print(festival_dict)

file.close()


lines = example.readlines()

count = 0


for line in lines:
    flag = 0
    for fest in festival_dict:
        # if fest in line and '||' + fest + '/DATETIME' in line:
        if fest in line and fest + '/DATETIME' in line:
            if flag == 0:
                line_replaced = line.replace(fest + '/DATETIME', fest + '/FESTIVAL')
                flag = 1
                print(line_replaced)
                count += 1
            else:
                line_replaced = line_replaced.replace(fest + '/DATETIME', fest + '/FESTIVAL')
                flag = 1
                print(line_replaced)
                count += 1
        else:
            if flag == 0:
                line_replaced = line
    result.write(line_replaced)

print(count)



example.close()
result.close()