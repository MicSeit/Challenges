import numpy as np

np.random.seed(42)

l1 = np.random.randint(1, 99, 100)
l2 = np.random.randint(1, 99, 100)
l3 = np.random.randint(1, 99, 100)

def intersection(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))
    
print(intersection(l1, l2, l3))
print(l1)
print(l2)
print(l3)
