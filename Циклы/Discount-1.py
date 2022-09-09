p = float(input())
t = 0
while p >= 0:
    if p >= 1000:
        p = p - p * 0.05
    t = t + p
    p = float (input())
print (t)