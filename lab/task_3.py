import numpy as np

n = int(input())

matrix = np.array([[0, 1],
                   [1, 3]], dtype=np.int64)

C = 10**9 + 7


def fast_exp(mat, n):
    if n == 0:
        return np.identity(2, dtype=np.int64)
    result = np.identity(2, dtype=np.int64)
    n_bin = []
    x = n
    while x > 0:
        n_bin.append(x % 2)
        x = x//2
    n_bin.reverse()
    for i in n_bin:
        result = np.dot(result, result) % C
        if i == 1:
            result = (result @ mat) % C

    return result




v = np.array([2, 3], dtype=int)


w = fast_exp(matrix, n - 1).dot(v) % C
print(w[0])

res = [2, 3]
res_fast = [2, 3]
for i in range(50):
    res.append((3 * res[-1] + res[-2]) % C)
    res_fast.append(fast_exp(matrix, i + 2).dot(v)[0] % C)

print(res)
print(res_fast)
X = np.array([200477279, 662131473])
print((matrix.dot(X)))
print(((3 * 662131473) + 200477279))