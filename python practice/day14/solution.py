# Difference class: Store positive integers 
class Difference:
    # elements: integer array
    def __init__(self, elements):
        self.elements = elements

# computeDifference method: Find the maximum difference between any 2 elements        
    def computeDifference(self):
        # maximumDifference: The maximum absolute difference
        self.maximumDifference = abs(max(self.elements) - min(self.elements))

# Enter the number of integers
size = input()
# Enter the elements array
elements = [int(x) for x in input().split(' ')]

N = Difference(elements)
N.computeDifference()

# Printout the maximum absolute difference between any 2 numbers in N
print(N.maximumDifference)
