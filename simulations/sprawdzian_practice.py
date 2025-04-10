import numpy as np
from scipy.stats import norm

cdf = norm.cdf


def binom_coef(n,k) -> int:
    a = 1
    for i in range(1,k+1):
        a = a*((n-i+1)/i)
    return int(a)


x = np.random.standard_normal(1000000)
y = np.random.standard_normal(1000000)
z = np.random.standard_normal(1000000)

s = (x + y + z) / 3
print(np.mean(s < 2))
print(np.mean(x < 2))

print(cdf(2 * np.sqrt(3)))
print(cdf(2))


