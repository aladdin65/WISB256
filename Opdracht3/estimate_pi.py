import sys
import random
import math
N = 0
L = 0
seed = 0

try:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
except:
    print("Use: estimate_pi.py N L")
    sys.exit()
try:
    seed = int(sys.argv[3])
    random.seed(seed)
except:
    seed = 0

def drop_needle(Lenght):
    x1 = random.random()
    a = random.vonmisesvariate(0, 0)
    x2 = x1 + Lenght * math.cos(a)
    if (x2 <= 0) or (x2 >= 1): return True
    else: return False

count = 0
for i in range(0, N):
    if (drop_needle(L) == True): count = count + 1
if (count > 0):
    frac = count / N
    if (L <= 1):
        Pi =  2 * L / frac
    else:
        Pi = (2 * L) / (frac - 1) - (2 / (frac - 1)) * (math.sqrt(L ** 2 - 1) + math.asin(1 / L))
else: Pi = 0

print(count, "hits in", N, "tries")
print(str(Pi))