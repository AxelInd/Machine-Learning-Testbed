# -*- coding: utf-8 -*-
"""
A simple script to play videos which contain a given substring in vlc.
Useful for setting up quick playlists.
Assumes window install and access to the "start vlc" command line instruction.
"""
#handles file exploration
import os
#enables command line queries
import sys
import random
from subprocess import check_output

"""
Determines whether any of a list of possible substrings exists within a string.
@param string: the string to be searched
@param _list: the list of possible substrings
@return True if one of the substrings exists in the string, else False.
"""
def substringExistsFromList (string, _list):
    for i in _list:
        try:
            #string.index(i) throws an exception if it is not in the string
            string.index(i)
            return True
        except:
            pass
    return False

"""
generate a list of files from all subdirectories which both match the given
the target substring and are of an allowable extension type.
@param target: the substring to be found
return a list of all matching files including their path
"""

def getMatchingFiles(target):
    ALLOWABLEEXTENSIONS = ['.mp4','.wav','.avi']
    allFiles=[]
    for i,(currentDir, dirsInDir,filesInDir) in enumerate(os.walk(os.getcwd())): 
        matchingFilesInDir=[]
        for x in filesInDir:
            try:
                if x.lower().index(target)!=-1 and substringExistsFromList(x,ALLOWABLEEXTENSIONS):
                    matchingFilesInDir.append(str(currentDir)+"/"+str(x))
            except:
                pass
        allFiles=allFiles+matchingFilesInDir
    return allFiles
        
"""
Converts the list of matching files to a string, each entry is surrounged by
double quotation marks.
@param allFiles: a list of all matching files including their path
@param lengthLimit: the maximum length of the return string
@param _randomise: whether the results should be shuffled
@return a string of all the files we have selected
"""
def getFilesToOpenAsString (allFiles, lengthLimit=7600,_randomise=True):
    filesToOpen=""
    
    if _randomise:
        random.shuffle(allFiles)
    
    for i in allFiles:
        fileToOpen = "\"{}\"".format(i).replace("/","\\")
        if len(fileToOpen)+len(filesToOpen)<lengthLimit:
            filesToOpen = filesToOpen + " " + fileToOpen
    return filesToOpen

"""
create and execute a command line statement to play all videos containing a
given substring in vlc.
@param target: the substring to be found
@param _randomise: whether the results should be shuffled
"""
def generate(target="",_randomise=True):
    allFiles=getMatchingFiles(target)
    filesToOpen=getFilesToOpenAsString(allFiles,_randomise=True)
    
    #start works in the command line because vlc is a registered name
    command = "start vlc {}".format(filesToOpen)
    print ("LENGTH OF COMMAND",len(command))
    command=command.replace("/","\\")
    p = check_output(command, shell=True) 


generate(sys.argv[1])







