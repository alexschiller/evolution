import math

class memoize:
    def __init__(self, fn):
        self.fn, self.m = fn, {}
    def __call__(self, *k):
        if k not in self.m: self.m[k] = self.fn(*k)
        return self.m[k]


@memoize
def B(n, k):
    return 0 if k < 0 or k > n or n < 0 else (math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))

def E(n):
    return B(n, 2)

def G(n, k):
    return B(E(n), k)

@memoize
def answer(n, k):
    if k < n - 1 or k > E(n) or n < 0:
        return 0
    elif n<=1:
        return 1
    elif k==n-1:
        return n**(n-2)
    else:
        return (G(n, k) - sum(B(n-1,i-1) * G(n-i,k-j) * C(i,j)
                                for i in xrange(1,n)
                                for j in xrange(i-1,min(E(i),k)+1) ))


N = 5
K = E(N)
C(10,6)