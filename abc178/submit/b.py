a, b, c, d = map(int, input().split())

if a >= 0 and c >= 0:
    print(b*d)
else :
    ac = a*c
    ad = a*d
    bc = b*c
    bd = b*d
    nums = [ac,ad,bc,bd]
    print(max(nums))