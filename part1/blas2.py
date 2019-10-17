import argparse
import numpy as np
import time

parser = argparse.ArgumentParser()
parser.add_argument("n",type=int)
args = parser.parse_args()
n = args.n

x = np.random.rand(n)
res = np.zeros_like(x)
A = np.random.rand(n,n)

start = time.time()
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        res[i] += A[i,j]*x[j]
end = time.time()

print(n,end-start)
