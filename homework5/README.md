#第五次作业 (2013301020006 王野)
##1.摘要
利用欧拉方法求解微分方程
##2.背景介绍
欧拉方法：由于计算机只能计算离散值，所以只能采用计算机计算的离散值来无限的逼近连续值。欧拉方法是其中的一种近似方法，具有广泛的应用。
##3.正文
习题1.6：N[0]=1000,a=10,b=0时[代码](https://github.com/Bensmav/computationalphysics_N2013301020006/blob/master/homework5/population.py)如下：
<pre><code>N=[]
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
mpl.show()</code></pre>
图像如下：

![Alt b=0](https://github.com/Bensmav/computationalphysics_N2013301020006/blob/master/homework5/population1.png "b=0")

令b=0.01或b=0.001可得如下结果

![Alt b=0.01](https://github.com/Bensmav/computationalphysics_N2013301020006/blob/master/homework5/population2.png "b=0.01")

![Alt b=0.001](https://github.com/Bensmav/computationalphysics_N2013301020006/blob/master/homework5/population3.png "b=0.001")
##4.结论
可知当b=0时人口成指数增长，b不为0时，人口数量最终会有一个极限值，b为0.01时，人口数量不变，小于0.01时人口会先增加后稳定，推测b大于0.01时人口会先减少后稳定。
##5.致谢
感谢蔡浩老师关于U元素衰变的例子。
