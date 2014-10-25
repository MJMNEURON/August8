from sys import argv
import re
import string
import fileinput
import os
import glob
import numpy as np

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
       

#os.chdir('/Users/jiemei/Desktop/combined_v2/trial_updated/combined_apr08')

for iii in range (0, 4):  
	addpath='./falltest1/'+filename+'/csr'+str(iii+1)
	if not os.path.exists(addpath): 
		os.makedirs(addpath)
	pathsavefilerelay = './falltest1/'+filename+'/csr'+str(iii+1)+'/relay'
	if not os.path.exists(pathsavefilerelay): 
		os.makedirs(pathsavefilerelay)
	pathsavefilereticular = './falltest1/'+filename+'/csr'+str(iii+1)+'/reticular'
	if not os.path.exists(pathsavefilereticular): 
		os.makedirs(pathsavefilereticular)


#relayfile="falltest1/Bal/csr1/relay/csr1_01.dat"
#reticularfile="falltest1/Bal/csr1/reticular/csr1_01.dat"
#s=open('reticular_'+filename+'.hoc').write() 
contrastlevel=1
trialnum=1

for contrastlevel in range(1,5):
	for trialnum in range(1,11):	
		f=open('filename.txt','w')
		spiking='"contrast/cs'+str(contrastlevel)+'_0'+str(trialnum)+'.dat"'	
		saverelay='"falltest1/'+filename+'/csr'+str(contrastlevel)+'/relay/csr'+str(contrastlevel)+'_0'+str(trialnum)+'.dat"'
		savereticular='"falltest1/'+filename+'/csr'+str(contrastlevel)+'/reticular/csr'+str(contrastlevel)+'_0'+str(trialnum)+'.dat"'
		print savereticular
		print saverelay
		f.write('reticularfile='+savereticular+'\n')
		f.write('relayfile='+saverelay+'\n')	
		f.write('spiking='+spiking+'\n')	
		f.write('strdef spiking, relayfile, reticularfile\n')
		f.close()
		with open('filename.txt') as ref:
			for lines in ref:
				line_prepender('reticular_'+filename+'.hoc', lines)
				os.system('nrniv '+ 'reticular_'+filename+'.hoc')
		os.remove('reticular_'+filename+'.hoc')
		with open('./compiled/reticular_'+filename+'.hoc') as oldver, open('./reticular_'+filename+'.hoc','w') as newver:
			for line in oldver:
				newver.write(line) 
		trialnum=trialnum+1		
	else:
		contrastlevel=contrastlevel+1
		trialnum=1

os.remove('reticular_'+filename+'.hoc')		

resultrelay = []
for counter in range (1, 5):
	os.chdir('/Users/jiemei/Desktop/combined_v2/trial_updated/combined_apr08/falltest1/'+filename+'/csr'+str(counter)+'/relay')
	non_blank_count=0
	for subcounter in range (1, 11):
		with open('csr'+str(counter)+'_0'+str(subcounter)+'.dat') as csresult:
			for line in csresult:
				if line.strip():
					non_blank_count+=1
			count=float(non_blank_count)/10
	resultrelay.append(count)		
	print 'number of lines:', str(non_blank_count), '  ', 'average:', str(count)

resultreticular = []
for counter1 in range (1, 5):
	os.chdir('/Users/jiemei/Desktop/combined_v2/trial_updated/combined_apr08/falltest1/'+filename+'/csr'+str(counter1)+'/reticular')
	non_blank_count1=0
	for subcounter1 in range (1, 11):
		with open('csr'+str(counter1)+'_0'+str(subcounter1)+'.dat') as csresult:
			for line in csresult:
				if line.strip():
					non_blank_count1+=1
			count1=float(non_blank_count1)/10
	resultreticular.append(count1)		
	print 'number of lines:', str(non_blank_count1), '  ', 'average:', str(count1)
	
print 'relay spiking: '+str(resultrelay)
print 'reticular spiking: '+str(resultreticular)

os.chdir('/Users/jiemei/Desktop/combined_v2/trial_updated/combined_apr08')
