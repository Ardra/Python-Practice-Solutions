'''Problem 2: Write a function flatten_dict to flatten a nested dictionary
 by joining the keys with . character.'''
def flatten_dict(d, parent_key=None, result=None):
    if result is None:
        result = {}

    for key, value in d.iteritems():
        if isinstance(value, dict):
            parent_key = key
            flatten_dict(value, parent_key, result)
            parent_key = None
        else:
            if parent_key:
                key = '.'.join([parent_key, key])
                result[key] = value
            else:
                result[key] = value

    return result

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})