import argparse
import numpy as np
import time

parser = argparse.ArgumentParser()
parser.add_argument("n",type=int)
args = parser.parse_args()
n = args.n

B = np.random.rand(n,n)
A = np.random.rand(n,n)
res = np.zeros((n,n))

start = time.time()
for i in range(n):
    for j in range(n):
        for k in range(n):
            res[i,j] += A[i,k]*B[k,j]
end = time.time()

print(n,end-start)
