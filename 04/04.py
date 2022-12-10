with open('input.txt') as my_input:
    works = []
    for line in my_input:
        pair_work = line[:-1].split(',')
        # print(pair_work)
        new_pair_work = []
        for one_work in pair_work:
            index = one_work.find('-')
            # print(f"index: {index}")
            min = int(one_work[0:index])
            max = int(one_work[index + 1:])
            # print(min)
            # print(max)
            new_one_work = list(range(min, max + 1))
            new_pair_work.append(new_one_work)
        works.append(new_pair_work)
# print(works)
# =============part 1============
count = 0
for pair_work in works:
    check_1 = all(item in pair_work[0] for item in pair_work[1])
    check_2 = all(item in pair_work[1] for item in pair_work[0])
    if check_1 or check_2:
        count += 1
print(count)

# =============part 2============
count = 0
for pair_work in works:
    check = any(item in pair_work[0] for item in pair_work[1])
    if check:
        count += 1
print(count)