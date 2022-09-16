# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:11:35 2022

@author: juans
"""

import math

R=10**5 #Bit rate example #[bps]
SNR_dB=14; #Relacion señal a ruido, 


SNR_lin=10**(SNR_dB/10)
P_e=1/2*math.erfc(math.sqrt(SNR_lin)) #BER, 1/2*erfc(sqrt(SNR_lin)) #Errores por bit


E_s=P_e*R #Errores por segundo
T_error=1/E_s #Cada cuanto tiene errores



print("Errors per second:",E_s)