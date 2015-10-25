'''Problem 1: Write a program to list all files in the given directory.'''
import os
def listfiles(dir_name):
    import os
    list = os.listdir(dir_name)
    return list
def file_detail(dir_name):
    list = listfiles(dir_name)
    details = []
    for x in list:
        details.append(os.stat(dir_name+'/'+x))
    #print details
    for i in range(len(list)):
        print list[i]+'\t'+str(details[i][6])+'\t'+str(details[i][8])
