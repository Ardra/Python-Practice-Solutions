'''Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

>>> invertdict({'x': 1, 'y': 2, 'z': 3})
{1: 'x', 2: 'y', 3: 'z'}'''

def valuesort(dictionary):
    return [dictionary[x] for x in sorted(dictionary.keys())]

