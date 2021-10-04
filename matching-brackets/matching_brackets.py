open = '{[('
close = '}])'

def is_paired(str):
    s = list(str)
    b = []
    while s:
        x = s.pop(0)
        if x in open:
            x = close[open.index(x)]
            b.append(x)
        elif x in close:
            if not b or x != b[-1]:
                return False
            b.pop()
    return len(b) == 0