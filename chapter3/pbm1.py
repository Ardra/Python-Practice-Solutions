'''Problem 1: Write a program to list all files in the given directory.'''
def listfiles(dir_name):
    import os
    list = os.listdir(dir_name)
    return list
