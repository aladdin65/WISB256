import sys
import math
bestandsnaam = str(sys.argv[1])
file = open(bestandsnaam)
old = 0
new = 0
nOfTwin = 0
nOfPrimes = 0
C2 = 0.6601618
for line in file:
    nOfPrimes = nOfPrimes + 1
    old = new
    new = int(line)
    if old != 0 and new != 0 and new - old == 2: nOfTwin = nOfTwin + 1

N = new
print("Largest Prime = " + str(N))
print("-------------------------------- ")
print("pi(N)         =  " + str(nOfPrimes))
nLog = N / math.log(N)
print("N/log(N)      =  " + str(nLog))
print("ratio         =  " + str(nOfPrimes / nLog))
print("-------------------------------- ")
print("pi_2(N)       =  " + str(nOfTwin))
cNlog = 2 * C2 * N / (math.log(N) ** 2)
print("2CN/log(N)^2  =  " + str(cNlog))
print("ratio         =  " + str(nOfTwin / cNlog))