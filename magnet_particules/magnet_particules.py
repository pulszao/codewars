def doubles(maxk, maxn):
    ans = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            ans += (1 / (k * pow(n + 1, 2 * k)))
    return ans
