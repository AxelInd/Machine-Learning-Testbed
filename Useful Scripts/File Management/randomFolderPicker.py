# -*- coding: utf-8 -*-
"""
Selects a random subfolder of the current directory
@author: axelt
"""
import os
import random
folders=[]
for i, (dirpath, dirnames, filenames) in enumerate(os.walk(os.getcwd())):
    #print (i)
    #print ("filenames",filenames)
    justFolderName = dirpath.split("\\")
    folders.append(justFolderName[-1])
    
#print (folders)
toRead = random.choice(folders)
print ("You should read: ", toRead)
