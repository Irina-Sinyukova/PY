n = int (input())
iq = int (input())
print(0)
for n in range(1, n):
    y = int(input())
    if y > iq:
        print('>')
    elif y < iq:
        print('<')
    else:
        print(0)
    iq = (iq * n + y) / (n + 1)