import os
from itertools import chain
from glob import glob

directory = 'resources/text'

for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        f = open('%s/%s'%(directory,filename), 'r')
        text = f.read()
        f.close()

        lines = [text.lower() for line in filename]
        with open('%s/%s'%(directory,filename), 'w') as out:
            out.writelines(lines)
            out.close