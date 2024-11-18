#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 00:21:01 2024

@author: ubuntu
"""


import serialusM2M as s
import fonction_deplacement as fdd
import fonction_PID as pid
import fonction_Pos_Calage as pos
import Fonction_AX as AX
import AUTOM as atm
import RPi.GPIO as GPIO


serial_port = '/dev/ttyS0'
Baudrate=1000000
ttl9600=False
Timeout=10

ser=s.init_serial(Baudrate,serial_port,Timeout,False)

A=s.init_serial(Baudrate,'/dev/ttyUSB0',Timeout,False)

B=s.init_serial(Baudrate,'/dev/ttyUSB1',Timeout,False)


    
bielle=(AX.AX_get_pos("01",A ))
s.timer_s(0.1)
top1=(AX.AX_get_pos("02",A))
s.timer_s(0.1)
btm1=(AX.AX_get_pos("03",A))
s.timer_s(0.1)
top2=(AX.AX_get_pos("04",A))
s.timer_s(0.1)
btm2=(AX.AX_get_pos("05",A))
s.timer_s(0.1)
top3=(AX.AX_get_pos("06",A))
s.timer_s(0.1)
btm3=(AX.AX_get_pos("07",A))


print("__________________________________________________________\n"+"<"+bielle+"||    BRAS1    ||   BRAS2   ||    BRAS3   \n"+"__________________________________________________________\n"+"TOP           || "+top1+" || "+top2+" || "+top3+"\n"+"BTM           || "+btm1+" || "+btm2+" || "+btm3+"\n"+"__________________________________________________________\n")


bielle=(AX.AX_get_pos("01",B ))
s.timer_s(0.1)
top1=(AX.AX_get_pos("02",B))
s.timer_s(0.1)
btm1=(AX.AX_get_pos("03",B))
s.timer_s(0.1)
top2=(AX.AX_get_pos("04",B))
s.timer_s(0.1)
btm2=(AX.AX_get_pos("05",B))
s.timer_s(0.1)
top3=(AX.AX_get_pos("06",B))
s.timer_s(0.1)
btm3=(AX.AX_get_pos("07",B))

 
print("__________________________________________________________\n"+"<"+bielle+"||    BRAS1    ||   BRAS2   ||    BRAS3   \n"+"__________________________________________________________\n"+"TOP           || "+top1+" || "+top2+" || "+top3+"\n"+"BTM           || "+btm1+" || "+btm2+" || "+btm3+"\n"+"__________________________________________________________\n")
