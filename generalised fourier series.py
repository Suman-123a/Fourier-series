import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return np.pi-abs(x)
def coeff(k,xi,xf,ni):
    g=2/(xf-xi)

    xx,h=np.linspace(xi,xf,ni,retstep=True)

    yy1=f(xx)*(np.cos(k*np.pi*xx*g))
    yy2=f(xx)*(np.sin(k*np.pi*xx*g))

    s1=0
    for i in range(1,ni-1):
        s1 += yy1[i]

    s1= 2*s1

    s1= yy1[0]+s1+yy1[ni-1]
    s1= s1*(h/2)

    a= g*s1

    s2=0
    for i in range(1,ni-1):
        s2 += yy2[i]

    s2= 2*s2

    s2= yy2[0]+s2+yy2[ni-1]
    s2= s2*(h/2)

    b= g*s2

    return a,b

aa=[]
bb=[]

xi=-np.pi
xf=np.pi
ni=100

nt=8

for i in range(nt):
    k=i
    w= coeff(k,xi,xf,ni)

    aa.append(w[0])
    bb.append(w[1])


xx=np.linspace(xi,xf,ni)

ff=[]
g=2/(xf-xi)
for i in range(ni):
    x=xx[i]

    s=(aa[0])/2
    for j in range(1,nt):
        p=aa[j]*np.cos(j*np.pi*x*g)
        q=bb[j]*np.sin(j*np.pi*x*g)

        s= s+p+q
    
    ff.append(s)
z1=np.linspace(-np.pi,np.pi,100)
y1=f(z1)
plt.axhline()
plt.axvline()
plt.plot(xx,ff)
#actual function
plt.plot(z1,y1)
plt.show()
print("first 10 a(n) fourier coefficient=",aa)
print("first 10 b(n) fourier coefficient",bb)