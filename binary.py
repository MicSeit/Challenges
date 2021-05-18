import numpy as np

np.random.seed(42)

l = np.random.randint(1, 99, 100)

def to_bits(n):
  return '{0:08b}'.format(n)

def reverse_num_bits(num: int):
    """
    :param n: A given number
    :return: A list with the binary equivalent of the number
    """
    binary_number = []
    # if end number is even and bigger than start the divide by 2
    while num > 0:
        if num % 2 == 0:
            bin= 0
    # if end number is even and bigger than start then add 1
        else:
            bin = 1
        binary_number.append(bin)
    return binary_number



print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000