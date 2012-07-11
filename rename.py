# A python script to rename more than one files in a directory.

# Usage : python rename.py <path> <new_name.extension>

# This script renames the files present in the directory given by <path> and places the renamed files in a directory called "pic_folder" that will be created within <path>.

# Example : Python rename.py /home/haris/pictures/tour/ tour.jpg

# Output : tour1.jpg, tour2.jpg, etc.

# FIXME
# -----

# I could not find a way to rename the files by keeping it within the existing directory itself. That is why I'm creating a new folder and moving the files to there. I'm working on it.

# Thank you!

import os
import sys

#Checking whehter path and filename are given.
if len(sys.argv) != 3:
    print "Usage : python rename.py <path> <new_name.extension>"
    sys.exit()

#Splitting name and extension.
name = sys.argv[2].split('.')
if len(name) < 2:
    name.append('')
else:
    name[1] = ".%s" %name[1]

#To name starting from 1 to number_of_files.
count = 1

#Creating a new folder in which the renamed files will be stored.
s = "%s/pic_folder" % sys.argv[1]
try:
    os.mkdir(s)
except OSError:
    #If pic_folder is already present, use it.
    pass

try:
    for x in os.walk(sys.argv[1]):
        for y in x[2]:
            #Creating the rename pattern.
            s = "%spic_folder/%s%s%s" %(x[0], name[0], count, name[1])
            #Getting the original path of the file to be renamed.
            z = os.path.join(x[0],y)
            #Renaming.
            os.rename(z, s)
            #Incrementing the count.
            count = count + 1
except OSError:
    pass
