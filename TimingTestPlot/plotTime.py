import matplotlib.pyplot as plt
from statistics import mean

plt.rcParams['text.usetex']=True
plt.rcParams['text.latex.preamble'] = '\\usepackage{amsmath}'


def get_time(vol):
  f=open('times.L'+str(vol)+'T'+str(2*vol)+'.dat','r')
  times=[]
  for line in f.readlines():
    times.append(float(line))
    
  return mean(times)


Ls=[]
times=[]
for L in [16,24,32,48,64]:
  Ls.append(L)
  times.append(get_time(L))

times[4]=times[4]*4


fig,ax1=plt.subplots()

pts1=ax1.plot(Ls, times, marker='o', markerfacecolor="None", markeredgecolor='C0', linestyle='None', label='Time')

ax1.set_yscale('log')

ax1.set_ylabel('$t\\,\\left[s\\right]$')
ax1.set_xlabel('$L$')

plt.title('HMC Single Trajectory time')
#plt.savefig('contract_time.pdf')
plt.savefig('trajectory_time.svg')
plt.show()
