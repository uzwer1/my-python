def digit_sum(n):
    x = str(n)
    r = 0
    for c in x:
        r += int(c)
    return r
    
print digit_sum(12345)