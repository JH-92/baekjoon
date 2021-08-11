import sys
input = sys.stdin.readline
cnt = int(input())

for _ in range(cnt):
    sentence = input()
    stack = []
    for word in sentence:
        if word == ' ' or word == '\n':
            print(''.join(stack[::-1]), end='')
            stack.clear()
            print(word, end='')
        else:
            stack.append(word)
