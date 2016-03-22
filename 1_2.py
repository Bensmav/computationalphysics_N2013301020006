x=[]
t=[]
v=40
dt=0.1
end_time=20
x.append(0)
t.append(0)
for i in range(int(end_time/dt)):
    tmp=x[i]+v*dt
    x.append(tmp)
    t.append(dt*(i+1))
    print t[-1],x[-1]
    
import matplotlib.pyplot as plt
plt.plot(t,x)
plt.xlabel('t(s)')
plt.ylabel('x(m)')
plt.show()
