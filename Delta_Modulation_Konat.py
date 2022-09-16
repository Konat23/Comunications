# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

   
def sgn(num):
    if num>0:
        return 1
    else:
        return -1

def encoder(lista): #si es 1 pasa 1 y si es -1 pasa a 0#
    salida=[]
    for element in lista:
        if element==1:
            salida.append(1)
            
        elif element==-1:
            salida.append(0)
        else:
            print("encoder invalid input");
            
    return salida
            

xqref=3; #el valor de x cuantizado que tomara como referencia (el primero es donde arranca)

xs=[3.9, 5.2, 6.7, 7.6, 8.2, 8.5, 8.5, 8.4, 7.9, 6.7, 5.5, 4.8, 4.1, 3.8, 3.2, 2.9, 2.5, 2.3, 1.9, 1.8, 1.5, 1.4, 1.5, 1.6, 1.9, 2.3, 2.7, 3.1, 3.6] #lista con los valores de la señal ya pasados por el zero holder
#xq=[] #donde se guardan los x cuantizados
eq=[] #se guardan los errores cuantizados, que en este caso es la salida que me intereza


delta=1; #paso de cuantizacion

for i in range(len(xs)):
    
    e=xs[i]-xqref #Calcula la diferencia entre la funcion y retenida y el anterior x cuantizado
    eq.append(delta*sgn(e))    #cuantiza el error, (dice si sube o si baja)
    xqref=xqref+eq[i]; #se actualiza el nuevo valor cuantizado con el que se va comparar
    
xDM=encoder(eq)
    

    
    
    
 
    

