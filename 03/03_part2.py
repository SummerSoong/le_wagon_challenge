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
        lists.append(line[:-1])

n = 3
group_lists = [lists[k:k+n] for k in range(0, len(lists), n)]
priorities = []
for lists in group_lists:
    common = set(lists[0]) & set(lists[1]) & set(lists[2])
    priority = get_priority(list(common)[0])
    priorities.append(priority)
print(sum(priorities))

