import os

os.chdir('/Users/jiemei/Desktop/combined_v2/trial_updated/combined_apr08')
s=open('latest.hoc').read()
for ii in range(0,10):
	s=s.replace('fspikes.ropen("contrast/cs4'+'_0'+str(ii)+'.dat")','fspikes.ropen("contrast/cs4'+'_0'+str(ii+1)+'.dat")')
#s2=s.replace('savspike.wopen("result_may11_relay[27]/gaba/csr4/csr4_09.dat")','savspike.wopen("result_may11_relay[27]/gaba/csr4/csr4_09.dat")')
	f=open('latest.hoc', 'w')
	f.write(s)
	print str(ii)
	s=s.replace('savspike.wopen("result_may24_relay[99]/gaba/csr4/csr4_0'+str(ii+1)+'.dat")','savspike.wopen("result_may24_relay[99]/gaba/csr4/csr4_0'+str(ii+2)+'.dat")')
	f=open('latest.hoc', 'w')
	f.write(s)
	print str(ii)
	f.close
	os.system('nrniv latest.hoc')
ii=ii+1

