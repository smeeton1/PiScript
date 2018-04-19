import os
import time
from sense_hat import SenseHat
import datetime


def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

sense = SenseHat()
sense.set_rotation(270)
while True:

 temp = sense.get_temperature_from_pressure()#
 temp=(temp+sense.get_temperature_from_humidity())/2
 t_c=get_cpu_temp()
 temp=temp-((t_c-temp)/2.3)
 temp = round(temp, 2)

 msg = "T=%s" % (temp)
 sense.show_message(msg,text_colour=[255,0,0])

 hum = sense.get_humidity()
 hum = round(hum, 2)

 msg = "H=%s" % (hum)
 sense.show_message(msg,text_colour=[0,255,0])

 p=sense.get_pressure()
 p=round(p,2)
 
 msg="P=%s" % (p)
 sense.show_message(msg,text_colour=[0,0,255])

 #print("t=%.1f  t_cpu=%.1f  h=%d  p=%d" % (temp, t_c, round(hum), round(p)))

 north = sense.get_compass()
 north = round(north,2)
 msg="N=%s" %(north)
 sense.show_message(msg,text_colour=[255,255,0])
 
 i = datetime.datetime.now()
 msg="t=%s:%s" %(i.hour,i.minute) 
 sense.show_message(msg,text_colour=[128,0,128])