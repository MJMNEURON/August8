import re
import string
import fileinput
import os
from sys import argv

script,filename=argv
filenameext=filename+'.txt'

params =['relret=', 'retrel=']
with open('reticularonly1.hoc') as oldver, open('reticular_'+filename+'.hoc','w') as newver:
    for line in oldver:
        if not any(param in line for param in params):
            newver.write(line)        


with open(filenameext) as inf:
    retrel = 0
    for line in inf:
        line = line.split('=')
        line[0] = line[0].strip()
  #      if line[0] == 'employee':
   #         employee = re.sub(r'[]\[\' ]','', line[1].strip()).split(',')

        if line[0] == 'retrel':
            retrel = float(line[1])

        elif line[0]=='relret':
            relret=float(line[1])
      ##  elif line[0] == 'managers':
        ##    managers = re.sub(r'[]\[\' ]','', line[1].strip()).split(',')

print retrel
print relret

def line_prepender(filename,line):
    with open(filename,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n') + '\n' + content)


line_prepender('reticular_'+filename+'.hoc', 'retrel=' + str(retrel))
line_prepender('reticular_'+filename+'.hoc', 'relret=' + str(relret))

os.system('nrngui '+ 'reticular'+filename+'.hoc')
