msg = input()
for msg_char in msg:
    if msg_char.isalpha():
        cur_pos = ord(msg_char) - ord('a')
        new_pos = (cur_pos + 13) % 26
        print(chr(new_pos + ord('a')), end='')
    else:
        print(msg_char, end='')
