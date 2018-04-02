#!/usr/bin/env python
import glob
import os
import time
# bgs= []
src='/home/habibi/Images/Background/'
timeout= 600 # soit 10 min (600 secondes)

def getFiles(extention):
    return glob.glob(src+'*.'+extention)

def addFilesIntoList(listeBgs, filesTakes):
    for file in filesTakes:
        listeBgs.append(file)

if __name__== "__main__":
   extentions = ['jpg', 'jpeg', 'png']
   bgs=[] # liste des backgrounds
   for extention in extentions:
       files = getFiles(extention)
       addFilesIntoList(bgs,files)
   while True:
       for bg in bgs:
           os.system('feh --bg-scale '+bg)    
           time.sleep(timeout)   
    

