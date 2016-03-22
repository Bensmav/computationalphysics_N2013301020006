#第四次作业
##1.摘要
利用欧拉方法求解微分方程
##2.背景介绍

##3.正文
习题1.2[代码](https://github.com/Bensmav/computationalphysics_N2013301020006/blob/master/chapter1/1_2.py)如下：
<pre><code>x=[]
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
plt.show()</code></pre>
