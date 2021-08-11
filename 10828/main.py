import sys
input = sys.stdin.readline
cnt = int(input())
stack = []
for _ in range(cnt):
    s = input().split()
    cmd = s[0]
    if cmd == 'push':
        num = int(s[1])
        stack.append(num)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if stack else 1)
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
