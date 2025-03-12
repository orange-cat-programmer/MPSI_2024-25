import numpy as np
samples = np.random.random(size=(100,5))
diff = samples[:,np.newaxis,:] - samples[np.newaxis,:,:]
distances = np.linalg.norm(diff,axis=-1)
#print(distances.shape)

from scipy.stats import norm

print(1-(2*norm.cdf(-3)))


