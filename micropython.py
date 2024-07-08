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
#T = Motor(Port.D)
L = Motor(Port.A)
R = Motor(Port.B)
slE = ColorSensor(Port.S2)
slD = ColorSensor(Port.S1)
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
V = 200 # velocidade (deg/s)
kP = 2
i = 1


 # coeficiente de correção
#Green = ?
Alibaba = DriveBase(L,R,wheel_diameter=55.5,axle_track=104)


while True:
    vlE = slE.reflection()
    vlD = slD.reflection()
    ev3.screen.print("E: ", vlE, "D: ", vlD) 
    vultS = ultS.distance()
    if vultS < 120:
        R.run_time(200,1000)
        wait(20)
        Alibaba.drive(200,200)
        wait(20)
        stop(300)
        wait()
        L.run_time(200,1200)
        wait(20)
    elif vlE < vlD:
        L.run(-10)
        R.run(V)
    elif vlD < vlE:
        R.run(-10)
        L.run(V)  
    elif vlD == vlE:
        R.run(V)
        L.run(V)
    else:
        L.run(0)
        R.run(0)
    

#robot = DriveBase(left_wheel,right_wheel,wheel_diameter=55.5,axle_track=104)
def VerLuz(): #mostrar os valores da luz identificada na tela

    ev3.screen.print("E: ", vcE, "D: ", vcD)

def Seguir1(): # Controle proporcional #corrige a direçâo que ele vai (continua seguindo a linha) (preto e branco)
    vlE = slE.reflection()
    vlD = slD.reflection() 
    ev3.screen.print("E: ", vlE, "D: ", vlD) 
    L.run(V)
    R.run(V)

def Seguir2():
    vlE = slE.reflection()
    vlD = slD.reflection()
    ev3.screen.print("E: ", vlE, "D: ", vlD) 
    if vlE < vlD:
        L.run(-10)
        R.run(V)
    elif vlD < vlE:
        R.run(-10)
        L.run(V)  
    elif vlD == vlE:
        R.run(V)
        L.run(V)
    else:
        L.run(0)
        R.run(0)
        
    while vultS > 50: 
        Alibaba.turn(245)
        wait(20)
        Alibaba.straight(210)
        wait(20)
        Alibaba.turn(-245)
        wait(20)
        Alibaba.straight(155)
        wait(20)

    


# def ICorG(): 
    # vlE = slE.reflection()
    # vlD = slD.reflection()
    # vcD = slD.color()
    # vcE = slE.color()
    # ev3.screen.print("E: ", vcE, "D: ", vcD)
    # if vcE == Green:
        # alibaba.turn(245)
    # elif vcD == Green:
        # alibaba.turn(-245)
    # elif vcE and vcD == Green:
        # alibaba.turn(590)
        
# def Modo_Cego():

# while True:
    

    
