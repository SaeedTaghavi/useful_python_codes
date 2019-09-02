import numpy as np
base_filename="file"
ext_filename=".txt"
for i in range(9,15):
    filename= 'file%02d.txt' % i
    # filename=base_filename+str(i)+ext_filename
    print (filename)