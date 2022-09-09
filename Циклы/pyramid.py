n = 13
space = n - 1
star = 1
for i in range(1, n + 1):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2