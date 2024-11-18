#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:19:00 2024

@author: ubuntu
"""


import serialusM2M as s
import fonction_deplacement as fdd
import fonction_PID as pid
import fonction_Pos_Calage as pos
import Fonction_AX as AX
import AUTOM as atm
import RPi.GPIO as GPIO


serial_port = '/dev/ttyAMA0'
Baudrate=1000000
ttl9600=False
Timeout=100



ser=s.init_serial(Baudrate,serial_port,Timeout,False)

A=s.init_serial(Baudrate,'/dev/ttyAMA1',Timeout,False)

B=s.init_serial(Baudrate,'/dev/ttyAMA2',Timeout,False)
msg_SCR="00"

vtours="100"
fdd.Evitement_on_off(False,ser)

print(pid.set_PID_VITESSE_DIST("09000","11900","04800",ser))
#print(pid.set_PID_VITESSE_DIST("01400","00200","07000",ser))


print(pid.set_MAX_ERREUR_INTEGRALLE_V("030000",ser))
print(pid.set_MAX_E_INTEGRALLE_BRAKE("000700",ser))


print(pid.set_VITESSE_CONSIGNE_MAX_MM("30",ser))
print(pid.set_VITESSE_DISTANCE_MIN("000750",ser))
print(pid.set_VITESSE_MAX_MM_TENSION("0230",ser))
print(pid.set_DISTANCE_CONSIGNE_MM("200000",ser))

print(pid.set_ACC_POSITION_CONSIGNE("2000", ser))
print(pid.set_ACC_POSITION_MIN("1000", ser))

print(pid.set_DCC_POSITION_CONSIGNE("2000", ser))
print(pid.set_DCC_POSITION_MIN("0300", ser))



print(pid.set_VITESSE_ANGLE_MAX("0080",ser))
print(pid.set_VITESSE_ANGLE_MIN("0010",ser))
print(pid.set_ACC_ORIENTATION_CONSIGNE("0300",ser)) # 2
print(pid.set_DCC_ORIENTATION_CONSIGNE("0600",ser))  # 6
print(pid.set_ACC_ORIENTATION_MIN("0200",ser))      # 2
print(pid.set_DCC_ORIENTATION_MIN("0400",ser))      # 4




GPIO.cleanup()

GPIO.setmode(GPIO.BCM)



GPIO.setup(21, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(12, GPIO.IN)
print(pos.get_Couleur(ser))


print(pos.set_Couleur(str(GPIO.input(19)),ser))

while(GPIO.input(12)):
    pass

atm.Init_AX(A)
atm.Init_AX(B)

pos.Callage_X("0140","000","0","030",ser)
print(pos.get_pos(ser))
fdd.avancer("0100","030",ser)
print(pos.get_pos(ser))
fdd.orienter("090","050",ser)
pos.Callage_Y("0140","090","0","030",ser)
fdd.avancer("0860","040",ser)
fdd.orienter("000","050",ser)

#atm.stock_plante("1","1","1",A)
##
##
#atm.destock_plante("1","1","1",A)
##
#atm.close_servo(B)
while((GPIO.input(21))):
    #print("waiting")
    pass
fdd.Start_match(ser)
fdd.Evitement_on_off(True,ser)

#atm.Start_turbune("0","0","1",A)
#s.timer_s(5)
#atm.Stop_turbune("0","0","1",A)
#atm.Start_turbune("1","1","1",A)

fdd.rejoindre("300","1700","1","100",ser)
fdd.orienter("090","050",ser)
atm.open_servo(B)
fdd.rejoindre("700","1700","1","100",ser)
atm.close_servo(B)

atm.open_servo(B)
fdd.reculer("0500","030",ser)

''''
fdd.rejoindre("1000","1000","1","100",ser)
fdd.orienter("090","050",ser)
fdd.avancer2("0180","050",ser)
#atm.Start_capteur(B)
ser.flush()
fdd.set_Break(ser)
fdd.rejoindre("1000","0820","0","050",ser)
fdd.rejoindre("1000","1280","1","050",ser)
atm.stock_plante("1","1","1",B)
fdd.rejoindre("1000","0720","0","050",ser)
atm.stock_plante("1","1","1",A)
fdd.rejoindre("1000","1000","1","100",ser)
fdd.orienter("000","050",ser)
fdd.rejoindre("0200","1000","0","100",ser)

for i in range(100):
    fdd.avancer("0100","030",ser)
    fdd.reculer("0100","030",ser)

'''