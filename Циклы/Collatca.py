n = int (input())
sum = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
        sum += 1
    else:
        n = 3 * n + 1
        sum += 1
print (sum)
    
    