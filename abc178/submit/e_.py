import numpy as np
from scipy.spatial.distance import cityblock


N = int(input())
s = [list(map(int, input().split())) for i in range(N)]

max = 0
for i in len(N):
    for j in len(N):
        # if s[i] == s[j]:
        #     continue
        # else:
        cb = abs(s[i][0] - s[j][0]) + abs(s[i][1] - s[j][1])
        if cb > max:
            max = cb
print(max)
