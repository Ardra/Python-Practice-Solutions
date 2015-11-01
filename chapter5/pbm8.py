'''Problem 8: Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.'''
def peep(item):
    item=list(item)
    element=item[0]
    return element,item
