def perms(lst):
    if len(lst) <=1:
        yield lst
    else:
        for p in perms(lst[1:]):
            for i in range(len(lst)):
                yield p[:i] + [lst[0]] + p[i:]