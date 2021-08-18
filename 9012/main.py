def valid_vps(vps):
    count = 0
    for ps in vps:
        if ps == '(':
            count += 1
        elif ps == ')':
            count -= 1
        if count < 0:
            return "NO"
    if count == 0:
        return "YES"
    else:
        return "NO"


cnt = int(input())
for _ in range(cnt):
    print(valid_vps(input()))




