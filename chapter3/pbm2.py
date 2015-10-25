'''Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.'''
def listfiles(dir_name):
    import os
    list = os.listdir(dir_name)
    return list

def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


def ext_count(dir_name):
    list1 = listfiles(dir_name)
    #print list1
    list2 = []
    for x in list1:
        list2.append(x.split('.'))
    #print list2
    list3 = []
    for x in list2:
        if(len(x)>1):
            list3.append(x[1])
    return word_frequency(list3)
    
