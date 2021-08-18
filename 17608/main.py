import sys
input = sys.stdin.readline
cnt = int(input())
stack = []
for _ in range(cnt):
    stack.append(int(input()))

fin = stack.pop()
count = 1
for _ in range(cnt-1):

    block = stack.pop()
    if block > fin:
        count += 1
        fin = block

print(count)