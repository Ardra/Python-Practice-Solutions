'''Problem 38: Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

>>> invertdict({'x': 1, 'y': 2, 'z': 3})
{1: 'x', 2: 'y', 3: 'z'}'''

def invertdict(dictionary):
    new_dict = {}
    for key, value in a.items():
        #print key, value
        new_dict[value]=key
        #print new_dict
        
    return new_dict
