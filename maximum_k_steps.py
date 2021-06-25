import numpy as np
import random

def max_k_steps(list,k):
    """
    : list:     a given list with only integers
    : k:        a given positive (non-zero) integer
    : return:   a list
    """
    sorted = np.sort(list)


    sublist = []
    elements = [min(sorted)]
    sublist.append(elements)
    
    differences = [list[i+1]-list[i] for i in range(len(list)-1)]

    #for k  max(differences) > 

    for elem in sorted:
        if k - 1 >= differences:
            sublist.append(elem)
        else:
            sublist.append([elements])

    return sublist

### Testing 

example = random.sample(range(0,100), 100)
k = 4
print(sublist(example, k))