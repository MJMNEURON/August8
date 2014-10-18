from sys import argv
import re
import string
import fileinput
import os


script,filename=argv
filenameext=filename+'.txt'

def line_prepender(filename,line):
    with open(filename,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)

with open('./base/reticularonly.hoc') as oldver, open('./compiled/reticular_'+filename+'.hoc','w') as newver:
    for line in oldver:
        newver.write(line)        

with open('./param/'+filenameext) as inf:      
    retrel = 0
    for line in inf:
        line_prepender('./compiled/reticular_'+filename+'.hoc', line)

with open('./compiled/reticular_'+filename+'.hoc') as oldver, open('./reticular_'+filename+'.hoc','w') as newver:
    for line in oldver:
        newver.write(line) 
       
os.system('nrngui '+ 'reticular_'+filename+'.hoc')
os.remove('reticular_'+filename+'.hoc')