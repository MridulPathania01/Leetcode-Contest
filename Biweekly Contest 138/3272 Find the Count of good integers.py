import math
class Solution:
    def __init__(self):
        self.f = [math.factorial(i) for i in range(11)]
    def g(self, n):
        p = []
        if n == 0:
            return p
        h = (n + 1) // 2
        s = 10 ** (h - 1)
        e = 10 ** h - 1
        if n == 1:
            s = 0
        for x in range(s, e + 1):
            y = str(x)
            z = ""
            if n % 2 == 0:
                r = y[::-1]
                z = y + r
            else:
                t = y[:-1][::-1]
                z = y + t
            if len(z) == n:
                q = int(z)
                p.append(q)
        return p
    def c(self, x, n):
        d = [0] * 10
        y = str(x).zfill(n)
        
        for z in y:
            d[int(z)] += 1
        return d

    def p(self, d, n):
        c = 0
        for x in range(1, 10):
            if d[x] == 0:
                continue
            
            a = d[:]
            a[x] -= 1
            v = all(f >= 0 for f in a)
            
            if not v:
                continue
            
            m = self.f[n - 1]
            for i in range(10):
                m //= self.f[a[i]]
            c += m
        return c
    def countGoodIntegers(self, n: int, k: int) -> int:
        p = self.g(n)
        v = [x for x in p if x % k == 0]
        u = set(tuple(self.c(x, n)) for x in v)
        t = 0
        for d in u:
            t += self.p(list(d), n)
        return t