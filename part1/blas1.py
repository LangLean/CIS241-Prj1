
import argparse
import numpy as np
import time

parser = argparse.ArgumentParser()
parser.add_argument("n",type=int)
args = parser.parse_args()
n = args.n

x = np.random.rand(n)
y = np.random.rand(n)
res = 0

start = time.time()
for i in range(n):
    res += x[i]*y[i]
end = time.time()

print(n,end-start)
