my_input = list(open('input.txt'))
folder = []
dir_size = {}
length = len(my_input)

# create a folder to save all directories
for line in my_input:
    if line[:3] == 'dir':
        dir_name = line[4:-1]
        if {dir_name: []} not in folder:
            folder.append({dir_name: []})
# folder.append({"/":[]})
# print(f'len of folder: {len(folder)}')
# print(folder)

# create a dict to save all sizes of files
file_size = {}
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
for line in my_input:
    if line[0] != '$':
        size = line.split()[0]
        if hasNumbers(size):
            file = line.split()[1]
            file_size.update({file: int(size)})
# print(file_size)

for item in folder:
    dir_name = list(item.keys())[0]
    # print(dir_name)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def find_size(dir_name):
    # print(dir_name)
    size = 0
    for i, line in enumerate(my_input):
        if line == f'$ cd {dir_name}\n':
            j = 2
            while i+j < length and my_input[i+j][0] != '$':
                sub_dir = my_input[i+j].split()
                if hasNumbers(sub_dir[0]):
                    size += int(sub_dir[0])
                else:
                    size += find_size(sub_dir[1])
                j += 1
    return size

dir_size = {}
# add size if all values are number and
for dir in folder:
    dir_name = list(dir.keys())[0]
    value = list(dir.values())[0]
    if all(isinstance(item, int) for item in value):
        sum = 0
        for item in value:
            sum += item
        dir_size.update({dir_name: sum})
# print(f'DIR_SIZE {dir_size}')

# make each dir value as the contents
# print(f'**********folder with empty size*********\n {folder}')
for dir in folder:
    dir_name = list(dir.keys())[0]
    for i, line in enumerate(my_input):
        if line == f'$ cd {dir_name}\n':
            j = 2
            sum = 0
            while i+j < length and my_input[i+j][0] != '$':
                content = my_input[i+j].split()[1]
                dir[dir_name].append(content)
                j+=1
# print(f'**********folder with contents*********\n {folder}')

for dir in folder:
    # print(f'DIR {list(dir.keys())[0]}')
    dir_size = list(dir.values())[0]
    dir_size_sum = 0
    for item in dir_size:
        if item in file_size:
            dir_size_sum += file_size[item]
        else:
            dir_size_sum += find_size(item)
    # print(f'sum: {dir_size_sum}')
    dir[list(dir.keys())[0]] = dir_size_sum

print(folder)