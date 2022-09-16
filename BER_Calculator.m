%{
Programa que recibe la relacion de señal a ruido y el Bit-Rate y regresa los Errores por 
segundo que puede tener al trasmitirse 
%}
SNR_dB=14;
SNR_lin=10^(SNR_dB/10);

%BER, 1/2*erfc(sqrt(SNR_lin)) #Errores por bit
P_e=1/2*erfc(sqrt(SNR_lin)); 