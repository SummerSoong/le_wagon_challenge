def find_first_start_of_packet_marker(text):
    for i, letter in enumerate(text):
        # print(text[i: i+4])
        # print(set(text[i: i+4]))
        if len(set(text[i: i+4])) == 4:
            return i+4

def find_first_start_of_message_marker(text):
    for i, letter in enumerate(text):
        # print(text[i: i+14])
        # print(set(text[i: i+14]))
        if len(set(text[i: i+14])) == 14:
            return i+14

with open('input.txt') as my_input:
    text = my_input.read()
    print(find_first_start_of_packet_marker(text))
    print(find_first_start_of_message_marker(text))
