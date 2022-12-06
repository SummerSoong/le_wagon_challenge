with open('input.txt') as my_input:
    lines = []
    sum = 0
    for i, line in enumerate(my_input):
        if line != '\n':
            line = int(line.strip('\n'))
            sum += line
        if line == '\n':
            lines.append(sum)
            sum = 0
    top = max(lines)
    print(top)
    lines.remove(top)
    second = max(lines)
    print(second)
    lines.remove(second)
    third = max(lines)
    print(third)
print(top + second + third)
