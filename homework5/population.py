N=[]
t=[]
a=10
b=0
N.append(1000)
t.append(0)
dt=0.01
end_time=1
for i in range(int(end_time/dt)):
	tmp=N[i]+(10*N[i]-b*(N[i]**2))*dt
	N.append(tmp)
	t.append(t[i]+dt)
	print t[-1],N[-1]
	
import matplotlib.pyplot as mpl
mpl.plot(t,N)
mpl.xlabel('t/year')
mpl.ylabel('N')
mpl.show()