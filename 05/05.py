stacks = []
with open('input.txt') as my_input:
    for line in my_input:
        stack = list(line[:-1])
        stack.reverse()
        stacks.append(stack)

# print(stacks)

instructions = []
with open('instruction.txt') as my_input:
    for line in my_input:
        instruction = line.split()
        instruction_nums = []
        for word in instruction:
            if word.isdigit():
                instruction_nums.append(int(word))
        instructions.append(instruction_nums)

# print(instructions)

def update_stack_1(num, source, goal):
    for i in range(0, num):
        move = stacks[source - 1].pop()
        stacks[goal - 1].append(move)
    # print(stacks)

def update_stack_2(num, source, goal):
    move = stacks[source - 1][(-num):]
    # print(move)
    stacks[source - 1] = stacks[source - 1][:(-num)]
    # print(stacks[source - 1])
    # print(stacks[goal - 1])
    stacks[goal - 1].extend(move)
    # print(stacks)

for instruction in instructions:
    num = instruction[0]
    source = instruction[1]
    goal = instruction[2]
    update_stack_2(num, source, goal)
# print(stacks)

result = ""
for stack in stacks:
    result += stack[-1]
print(result)