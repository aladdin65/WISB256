import math
import sys
import time
N = int(sys.argv[1])
bestandsNaam = str(sys.argv[2])
file = open(bestandsNaam, 'w')
lijst = [True for x in range(0, N + 2)]
T1 = time.perf_counter()
for i in range(2, int(math.ceil(math.sqrt(N)))):
    if lijst[i] != False:
        for j in range(2, math.ceil(N // i) + 1):
            lijst[j * i] = False
count = 0
for i in range(2, N):
    if lijst[i] != False:
        file.write(str(i) + "\n")
        count = count + 1
T2 = time.perf_counter()
timeElapsed = T2 - T1
file.close
print("Found", count, "Prime numbers smaller than", N, "in", timeElapsed)