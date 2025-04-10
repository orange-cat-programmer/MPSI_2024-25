import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

res = []
sumy = []
meow = []
last = []

for i in range(100000):
    suma = 0
    roll = np.random.choice([1, 2, 3, 4, 5, 6])
    suma += roll
    count = 1
    while True:
        new_roll = np.random.choice([1, 2, 3, 4, 5, 6])
        if new_roll <= roll:
            last.append(roll)
            meow.append(new_roll)
            break
        roll = new_roll
        suma += new_roll
        count += 1
    res.append(count)
    sumy.append(suma)

last = np.array(last)
plt.hist(last, bins=6, density=True, edgecolor='black')
plt.show()

counts_last = np.bincount(last, minlength=7)[1:]

aid = np.sum((counts_last/np.sum(counts_last)) * np.array([(k+1)/2 for k in range(1,7)]))



print(sum(sumy)/len(sumy))

a = [0]*7
a[0] = 1
a[1] += 1/2 * 5/6
a[2] += 1/6 * 5/6 * 4/6
a[3] += 1/24 * 5/6 * 4/6 * 3/6
a[4] += 1/120 * 5/6 * 4/6 * 3/6 * 2/6
a[5] += 1/720 * 5/6 * 4/6 * 3/6 * 2/6 * 1/6

theoretical = sum(a)
sum_theoretical = (theoretical + 1) * 3.5 - aid
print(sum_theoretical)
print('\n')
print(theoretical)













