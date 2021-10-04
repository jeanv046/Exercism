def slices(series, i):
    if i < 1 or i > len(series):
        raise ValueError(
            'slice size must be in interval [2,{}]'.format(len(series))
        )
    ints = [int(x) for x in series]
    return [
        ''.join(map(str, ints[x:i + x]))
        for x in range(len(series) - i + 1)
    ]