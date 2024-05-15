#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Create your objects here.
ev3 = EV3Brick()
#Four_motor = Motor(Port.A)
#Three_motor = Motor(Port.C)
left_wheel = Motor(Port.D)
right_wheel = Motor(Port.B)
#slE = ColorSensor(Port.S1)
#slD = ColorSensor(Port.S2)
#ultS = UltrasonicSensor()
#vlE = slE.reflection() # valor de reflexão esquerdo
#vlD = slD.reflection() # valor de reflexão direito
#amB1 = slD.ambient()
#amB2 = slE.ambient()
#vcD = slD.Color() # valor de cor direito
#vcE = slE.Color() # valor de cor esquerdo
#vlDE = vlE + vlD
V = 200 # velocidade (deg/s)
kP = 15 # coeficiente de correção
#lPreto =  # valor de cor preta
#vlPreto =  20 # valor de reflexão branca
#slBranco =   # valor de cor branca 
#vlBranco =  80 # valor de reflexão branca
# Write your program here.
Alibaba = DriveBase(left_wheel, right_wheel, wheel_diameter=55.5, axle_track=104)

#robot = DriveBase(left_wheel,right_wheel,wheel_diameter=55.5,axle_track=104)
Alibaba = DriveBase(left_wheel, right_wheel, wheel_diameter=55.5, axle_track=104)
def Test():
Alibaba.turn(245)
Alibaba.straight(210)
Alibaba.turn(-245)
Alibaba.straight(155)
Alibaba.run_time(190, 10000)   

def VerLuz():
    ev3.screen.print("E: ",vlE," D: ",vlD)


def CProp(): # Controle proporcional
    vlE = slE.reflection()
    vlD = slD.reflection()
    MgEr = vlE - vlD # Margem de Erro
    P = MgEr * kP # 
    left_wheel.run(V + P)
    right_wheel.run(V - P)
    if vlE == vlD:
        left_wheel.run(V + P)
        right_wheel.run(V - P)
        

def VerifiDistancia ():
  ultS = UltrasonicSensor()
  if  ultSF > 100:
    Alibaba.turn(245)
    Alibaba.straight(210)
    Alibaba.turn(-245)
    Alibaba.straight(155)

def 

    
while True:
   # verificarLuz()
    VerLuz() 
    Test()
