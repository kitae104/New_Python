def add_up(values):
    s = 0
    for v in values:
        s += v
    return s

print(add_up([1,2,3]) == 6)