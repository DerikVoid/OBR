#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.
ev3 = EV3Brick()
#medium_motor = Motor(Port.D)
left_wheel = Motor(Port.A)
right_wheel = Motor(Port.D)
slE = ColorSensor(Port.S1)
slD = ColorSensor(Port.S2)
ultS = UltrasonicSensor()
vlE = slE.reflection() # valor de reflexão esquerdo
vlD = slD.reflection() # valor de reflexão direito
vcD = slD.Color() # valor de cor direito
vcE = slE.Color() # valor de cor esquerdo
vlDE = vlE + vlD
V = 200 # velocidade (deg/s)
kP = 15 # coeficiente de correção
slPreto =  # valor de cor preta
vlPreto =  20 # valor de reflexão branca
slBranco =   # valor de cor branca 
vlBranco =  80 # valor de reflexão branca
# Write your program here.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#robot = DriveBase(left_wheel,right_wheel,wheel_diameter=55.5,axle_track=104)

def VerLuz ():
    ev3.screen.print("E: ",vlE," D: ",vlD)


def CProp(): # Controle proporcional
    vlE = slE.reflection()
    vlD = slD.reflection()
    MgEr = vlE - vlD # Margem de Erro
    P = MgEr * kP # 
    left_wheel.run(V + P)
    right_wheel.run(V - P)
    

def VerifiDistancia ():
  ultS = UltrasonicSensor()
  if  ultSF > 100:
    left_wheel.stop(50)
    right_wheel.stop(50)
    
while True:
   # verificarLuz()
    CProp() 
