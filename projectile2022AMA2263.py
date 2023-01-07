#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# In[14]:


def projectile1(state, g, t, alpha):
  u1,u2, v1, v2 = state 
  du1=u2
  dv1=v2
  beta=np.arccos(u2/((u2**2+v2**2)**0.5))
#alpha includes all the constants like mass, density, drag coefficient and area;
#mass=1kg, density=1.2kg/m3, drag coefficient=0.5 and area=pi*(0.1)^2
#hence alpha=-0.00095
  du2=alpha*(u2**2+v2**2)*np.cos(np.rad2deg(beta))
  dv2=-g+alpha*(u2**2+v2**2)*np.sin(np.rad2deg(beta))
  return [du1, du2, dv1, dv2]


# In[15]:


g=9.81
alpha=-0.00095#The value of alpha which we calculated above
p=(g,alpha)
u0 = [0,20,0,30]#Initial conditions are to be given
t=np.linspace(0,120,100000)
result = odeint(projectile1, u0, t, p)


# In[16]:


#We need to introduce a loop to filter out the negative or excess values of y in the result
a=0
for i in range(0,len(result[:,0])):
   if result[i,2]<0:
     break
   a=a+1

b=4   

result2 = np.zeros((a,b))

for i in range(0,a):
  for j in range(0,4):
    result2[i,j]=result[i,j]


# In[17]:


#plotting of the projectile path 
fig1 = plt.figure(figsize= (10,8))
ax = fig1.gca()
ax.plot(result2[:,0], result2[:,2], label = 'plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.legend()


# In[18]:


g=9.81
alpha=-0.00095
p=(g,alpha)
V=10#taking a constant value of initial resultant velocity
maxi={}
for theta in range(0,91,1):

  u0 = [0,V*np.cos(np.deg2rad(theta)),0,V*np.sin(np.deg2rad(theta))]
  t=np.linspace(0,120,100000)
  result = odeint(projectile1, u0, t, p)
  a=0
  for i in range(0,len(result[:,0])):
    if result[i,2]<0:
      break
    a=a+1

  b=4   
  result2 = np.zeros((a,b))

  for i in range(0,a):
    for j in range(0,4):
      result2[i,j]=result[i,j]
     
  Xmax=result2[:,0].max()
  maxi[theta]=Xmax
Xmaxlist=[]
thetalist=[]
for k in range (0,91):
   Xmaxlist.append(maxi[k])
   thetalist.append(k)

fig1 = plt.figure(figsize= (12,8))
ax = fig1.gca()
ax.plot(thetalist,Xmaxlist, label = 'plot')
ax.set_xlabel('theta')
ax.set_ylabel('Xmax')
plt.legend()

#I have also tried and tested to make this curve very smoother using linspace but it is taking too long to run
#maxi2={}
#thet=np.linspace(0,90,10000)
#for th in thet:
#  u0 = [0,V*np.cos(np.deg2rad(th)),0,V*np.sin(np.deg2rad(th))]
#  t=np.linspace(0,120,100000)
#  result4 = odeint(projectile1, u0, t, p)
#  a=0
#  for i in range(0,len(result[:,0])):
#    if result4[i,2]<0:
#      break
#    a=a+1
#
#  b=4   
#  result5 = np.zeros((a,b))
#
#  for i in range(0,a):
#    for j in range(0,4):
#      result5[i,j]=result4[i,j]
#     
#  Xmax2=result5[:,0].max()
#  maxi2[th]=Xmax2
#Xmaxlist2=[]
#thetalist2=[]
#for th in thet:
#  Xmaxlist2.append(maxi2[th])
#  thetalist2.append(th)
#fig1 = plt.figure(figsize= (12,8))
#ax = fig1.gca()
#ax.plot(thetalist2,Xmaxlist2, label = 'plot')
#ax.set_xlabel('theta')
#ax.set_ylabel('Xmax')
#plt.legend()


# In[19]:


for j in range (0, 91):
  if Xmaxlist[j]==max(Xmaxlist):
    maxtheta=j
v0 = [0,V*np.cos(np.deg2rad(maxtheta)),0,V*np.sin(np.deg2rad(maxtheta))]
t=np.linspace(0,120,100000)
result3 = odeint(projectile1, v0, t, p)


# In[20]:


print(maxtheta) #prints the value of initial angle(theta) for the maximum range at initial velocity 10m/s


# In[21]:


a=0
for i in range(0,len(result[:,0])):
   if result3[i,2]<0:
     break
   a=a+1

b=4   

result4 = np.zeros((a,b))

for i in range(0,a):
  for j in range(0,4):
    result4[i,j]=result3[i,j]
     


# In[22]:


fig1 = plt.figure(figsize= (10,8))
ax = fig1.gca()
ax.plot(result4[:,0], result4[:,2], label = 'plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
#ax.plot(t, result[:,1], label = 'omega')
plt.legend()
#plotting the projectile for initial velocity=10 and initial angle=36(angle for max range)


# In[ ]:





# In[ ]:




