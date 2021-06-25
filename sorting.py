# Import the heapq library
import heapq as hp

# Define the function
def sort(list):
     x = []
     for number in list:
         hp.heappush(x, number)
     return [hp.heappop(x) for i in range(len(x))]

# Testing
#sort([1, 5, 9, 2, 0])
