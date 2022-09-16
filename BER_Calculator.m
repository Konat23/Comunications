SNR_dB=14;
SNR_lin=10^(SNR_dB/10);

%BER, 1/2*erfc(sqrt(SNR_lin)) #Errores por bit
P_e=1/2*erfc(sqrt(SNR_lin)); 