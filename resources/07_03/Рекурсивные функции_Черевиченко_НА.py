def r_fact(n):
    if n in (0, 1): return 1
    return n * r_fact(n - 1)


def d_fact(n):
    if n in (0, 1): return 1

    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def pow2(l):
    return list(num**2 for num in l)





