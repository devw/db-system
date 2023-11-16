import numpy as np

list = [1,2,3,4,5,6,7,8,9]

q1 = np.percentile(list, 25)
q2 = np.percentile(list, 50)
q3 = np.percentile(list, 76)

print("q1: ", q1)
print("q2: ", q2)
print("q3: ", q3)
