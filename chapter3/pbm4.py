'''Problem 4: Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree'''


def tree(dir_name):
    for root, dirs, files in os.walk(dir_name):
        print root
        print dirs
        print files
