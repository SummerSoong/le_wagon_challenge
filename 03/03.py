# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def get_priority(alphabet):
    if alphabet.islower():
        return ord(alphabet) - 96
    else:
        return ord(alphabet) - 38

with open("input.txt") as my_input:
    lists = []
    for line in my_input:
        # print(len(line) - 1)
        first_half = line[:int((len(line) - 1) / 2)]
        # print(first_half)
        last_half = line[int((len(line) - 1) / 2):]
        # print(last_half)
        common = set(first_half) & set(last_half)
        print(list(common)[0])
        lists.append(get_priority(list(common)[0]))

print(sum(lists))
