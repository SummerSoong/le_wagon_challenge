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
folder.append({"/":[]})
print(f'len of folder: {len(folder)}')
print(folder)

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

#calculate
for dir in folder:
    value = list(dir.values())[0]
    # print(f'value {value}')
    for file_or_dir in value:
        # if it is a file
        if file_or_dir in file_size:
            size = file_size[file_or_dir]
            # print(f"file name: {file_or_dir}")
            # print(f"size: {size}")
            value[value.index(file_or_dir)] = size

# print(f'**********folder with file sizes*********\n {folder}')


def update_dir_size():
# add size if all values are number and
    for dir in folder:
        dir_name = list(dir.keys())[0]
        value = list(dir.values())[0]
        if all(isinstance(item, int) for item in value):
            sum = 0
            for item in value:
                sum += item
            dir_size.update({dir_name: sum})
update_dir_size()
# print(f'********dir_size_original*******\n{dir_size}')
# print(f'len of dir_size:{len(dir_size)}')

def update_folder():
    for dir in folder:
        value = list(dir.values())[0]
        # print(f'value {value}')
        for dir_name in value:
            if isinstance(dir_name, str) and dir_name in dir_size:
                # print(dir_name)
                size = dir_size[dir_name]
                # print(size)
                value[value.index(dir_name)] = size

i = 0
while i <= 90:
    update_folder()
    update_dir_size()
    i+=1
# print(len(dir_size))



result = 0
final_dir = []
for dir in folder:
    dir_name = list(dir.keys())[0]
    dir_size_lists = list(dir.values())[0]
    dir_size = 0
    for size in dir_size_lists:
        dir_size += size
    final_dir.append({dir_name: dir_size})
# print(final_dir)
# print(len(final_dir))
result = 0
for item in final_dir:
    number = list(item.values())[0]
    if number <= 100000:
        result += number
print(result)
