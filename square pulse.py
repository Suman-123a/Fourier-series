#Fourier decomposition of Square Pulse
#f(x)=π(-π<x<0) and -π(0<x<π)
import numpy as np
import matplotlib.pyplot as plt

def coeff1(k,xi1,xf1,ni):
    g=1/np.pi

    xx,h=np.linspace(xi1,xf1,ni,retstep=True)

    yy1=(np.pi)*(np.cos(k*xx))
    yy2=(np.pi)*(np.sin(k*xx))

    s1=0
    for i in range(1,ni-1):
        s1 += yy1[i]

    s1= 2*s1

    s1= yy1[0]+s1+yy1[ni-1]
    s1= s1*(h/2)

    a1= g*s1

    s2=0
    for i in range(1,ni-1):
        s2 += yy2[i]

    s2= 2*s2

    s2= yy2[0]+s2+yy2[ni-1]
    s2= s2*(h/2)

    b1= g*s2

    return a1,b1

def coeff2(k,xi2,xf2,ni):
    g=1/np.pi

    xx,h=np.linspace(xi2,xf2,ni,retstep=True)

    yy1=-np.pi*(np.cos(k*xx))
    yy2=-np.pi*(np.sin(k*xx))

    s1=0
    for i in range(1,ni-1):
        s1 += yy1[i]

    s1= 2*s1

    s1= yy1[0]+s1+yy1[ni-1]
    s1= s1*(h/2)

    a2= g*s1

    s2=0
    for i in range(1,ni-1):
        s2 += yy2[i]

    s2= 2*s2

    s2= yy2[0]+s2+yy2[ni-1]
    s2= s2*(h/2)

    b2= g*s2

    return a2,b2

aa=[]
bb=[]

xi1=-np.pi
xf1=0
xi2=0
xf2=np.pi
ni=100

nt=50

for i in range(nt):
    k=i
    w1 = coeff1(k,xi1,xf1,ni)
    w2 = coeff2(k,xi2,xf2,ni)

    aa.append(w1[0]+w2[0])
    bb.append(w1[1]+w2[1])

xi=-np.pi
xf=np.pi

xx=np.linspace(xi,xf,ni)

ff=[]

for i in range(ni):
    x=xx[i]

    s=(aa[0])/2
    for j in range(1,nt):
        p=aa[j]*np.cos(j*x)
        q=bb[j]*np.sin(j*x)

        s= s+p+q
    
    ff.append(s)
z0=-np.pi
z1=0
n=100
h1=(z1-z0)/(n-1)
pp=[]
pp1=[]
for i in range(100):
	p=z0+i*h1
	pp.append(p)
	p1=np.pi
	pp1.append(p1)
z00=0
z11=np.pi
h2=(z11-z00)/(n-1)
uu=[]
uu1=[]
for i in range(100):
	u=z00+i*h2
	uu.append(u)
	u1=-np.pi
	uu1.append(u1)
plt.plot(uu,uu1)
plt.plot(pp,pp1)
plt.plot(xx,ff)
plt.axhline()
plt.axvline()
plt.show()