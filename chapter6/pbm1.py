'''Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.'''

def mul(x,y):
    if y==0:
        return 0
    elif y>0:
        return x+mul(x,y-1)
    

