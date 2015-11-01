import sys
import os
def python_files(dir):
    files=os.listdir(dir)
    for f in files:
        if '.py' in f:
            print f,len(open(f).readlines())
python_files(sys.argv[1])
