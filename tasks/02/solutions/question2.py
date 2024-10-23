# 2.https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

def findUnion(self, a, b):
    # Combine both arrays into one
    combined = a + b
    
    # Use a set to get distinct elements
    union_set = set(combined)
    
    # The length of the set is the number of distinct elements in the union
    return len(union_set)
