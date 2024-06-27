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
#Three_wheel = Motor(Port.C)
left_wheel = Motor(Port.A)
right_wheel = Motor(Port.B)
slE = ColorSensor(Port.S2)
slD = ColorSensor(Port.S3)
#slM = ColorSensor(Port.S4)
ultS = UltrasonicSensor(Port.S4)
vultS = ultS.distance()
vlE = slE.reflection() # valor de reflexão esquerdo
vlD = slD.reflection() # valor de reflexão direito
#vlM = slM.reflection() # valor de reflexão Meio
#amB1 = slD.ambient()
#amB2 = slE.ambient()
#amB3 = slM.ambient()
vcD = slD.color() # valor de cor direito
vcE = slE.color() # valor de cor esquerdo
#vcM = slM.color() # valor de cor Meio
#vlDE = vlE + vlD
V = -200 # velocidade (deg/s)
kP = -7 # coeficiente de correção
#Green = ?
Alibaba = DriveBase(left_wheel,right_wheel,wheel_diameter=55.5,axle_track=104)

#robot = DriveBase(left_wheel,right_wheel,wheel_diameter=55.5,axle_track=104)
def VerLuz(): #mostrar os valores da luz identificada na tela
    
    ev3.screen.print("E: ",vlE, "D :"vlD)

def CProp(): # Controle proporcional #corrige a direçâo que ele vai (continua seguindo a linha) (preto e branco)
    vlE = slE.reflection()
    vlD = slD.reflection()
    MgErE = vlD - vlE
    MgErD = vlE - vlD 
    if MgErE and MgErD == 0 # Margem de Erro
    left_wheel.run(V)
    right_wheel.run(V)
    elif MgErE and MgErD != 0
        B1 = MgErE * kP
        B2 = MgErD * kP 
        left_wheel.run(V + B1)
        right_wheel.run(V + B2)

    
        
#def VFD(): #identificar obstáculos
    #vultS = ultS.distance()
    #vultS == 20
    #Alibaba.turn(245)
    #Alibaba.straight(210)
    #Alibaba.turn(-245)
    #Alibaba.straight(155)

#def ICorG(): #identificar verde (para curvas)
    #if vcE == Green
    #alibaba.turn()

while True:
    CProp()
    
