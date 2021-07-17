import os
from graphics import *
import time
from sense_hat import SenseHat
import datetime

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

sense = SenseHat()
sense.set_rotation(270)


def main():
    win = GraphWin('Sense Hat', 450, 100)
    #win.yUp() # right side up coordinates
    win.setBackground('blue')
    message = Text(Point(60, 15), 'Temperature')
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(12)
    message.draw(win)

    message2 = Text(Point(160, 15), 'Humidity')
    message2.setTextColor('black')
    message2.setStyle('italic')
    message2.setSize(12)
    message2.draw(win)

    message3 = Text(Point(240, 15), 'Pressure')
    message3.setTextColor('black')
    message3.setStyle('italic')
    message3.setSize(12)
    message3.draw(win)

    message4 = Text(Point(320, 15), 'North')
    message4.setTextColor('black')
    message4.setStyle('italic')
    message4.setSize(12)
    message4.draw(win)

    message5 = Text(Point(400, 15), 'CPU')
    message5.setTextColor('black')
    message5.setStyle('italic')
    message5.setSize(12)
    message5.draw(win)
    
    go = True
    i = 1
    while go:
        tem = sense.get_temperature_from_pressure()#
        tem = (tem+sense.get_temperature_from_humidity())/2
        tem = round(tem, 1)

        temp = Text(Point(60, 60), round(sense.get_temperature_from_pressure()(),1))
        temp.setTextColor('black')
        temp.setSize(15)
        temp.draw(win)
        

        hum = Text(Point(160, 60), round(sense.get_humidity(),1))
        hum.setTextColor('black')
        hum.setSize(15)
        hum.draw(win)
        

        pres = Text(Point(240, 60), round(sense.get_pressure(),1))
        pres.setTextColor('black')
        pres.setSize(15)
        pres.draw(win)


        nort = Text(Point(320, 60), round(sense.get_compass(),1))
        nort.setTextColor('black')
        nort.setSize(15)
        nort.draw(win)

        cpu = Text(Point(400, 60), round(get_cpu_temp(),1))
        cpu.setTextColor('black')
        cpu.setSize(15)
        cpu.draw(win)


        time.sleep(1)
        temp.undraw()
        hum.undraw()
        pres.undraw()
        nort.undraw()
        cpu.undraw()

        i=i+1
        #if win.getMouse()
        #    go = False
        

    # Get and draw three vertices of triangle
    #cir2 = Circle(Point(150,125), 25)
    #cir2.setFill("red")
    #cir2.draw(win)



    #message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
