#!/usr/bin/env python
import os
import time
from sense_hat import SenseHat
import numpy as np
import matplotlib.pyplot as plt

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

temp=[]
temp2=[]
temp3=[]
temp4=[]
t_c=[]
hum=[]
p=[]
T=[]

t_o=time.time()
sense = SenseHat()
log=open("log.text","w+")
for i in range(50):
 T.append(round(time.time()-t_o,2))
 temp.append(round( sense.get_temperature_from_pressure(),2))
 temp2.append(round(sense.get_temperature_from_humidity(),2))
 temp3.append((temp[i]+temp2[i])/2)
 t_c.append(round(get_cpu_temp(),2))
 temp4.append(round(temp3[i]-((t_c[i]-temp3[i])/2.4),2))
 hum.append(round(sense.get_humidity(), 2))
 p.append(round(sense.get_pressure(),2))
 log.write("%s %s %s %s %s %s \n" %(T[i],temp[i],temp2[i],t_c[i],hum[i],p[i]))
 time.sleep(5)
 
plt.plot(T,temp,'r',label="$T_p$")
plt.plot(T,temp2,'b',label="$T_H$")
plt.plot(T,t_c,'g',label="$T_c$")
plt.plot(T,temp4,'y',label="$T_a$")
plt.ylabel('temperature')
plt.xlabel('time')
plt.legend(bbox_to_anchor=(0.8, 0.7), loc=2, borderaxespad=0.)
plt.savefig('temp.eps', format='eps', dpi=1000)
plt.clf()

plt.figure(1)
plt.subplot(211)
plt.plot(T,hum)
plt.ylabel('humidity')
plt.xlabel('time')
plt.subplot(212)
plt.plot(T,p)
plt.ylabel('pressure')
plt.xlabel('time')
plt.savefig('HP.eps', format='eps', dpi=1000)
plt.clf()