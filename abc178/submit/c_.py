N = int(input())
T = 10 ** 9 + 7
nCr = {}


def cmb(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in nCr:
        return nCr[(n, r)]
    nCr[(n, r)] = cmb(n-1, r) + cmb(n-1, r-1)
    return nCr[(n, r)]

if N == 1:
    print(0)
else:
    # NC2
    total = cmb(N,2)
    print(total % T)
    # 10^n - 10C8  - 10C9 - 10C9
    # total = 10 ** N - (10*9) - 10
    # ans = total % T
    # print(ans)

