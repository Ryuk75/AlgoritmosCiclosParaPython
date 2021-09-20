# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:44:22 2021

@author: ricar
"""
# Taller de algoritmos Ciclos Para

#1. El departamento de Seguridad de Transito de Barranquilla, desea saber de
#los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
#color. Conociendo el último digito de la placa de cada automóvil se puede
#determinar el color de la calcomanía
print("1/ Determine cuantos carros entran con calcomania de cada color")
rosa = 0
amarillo = 0
rojo = 0
verde = 0
azul = 0
numeroCarros = int(input("Cuantos carros ingresaron a la ciudad: "))
for i in range(numeroCarros):
    color = int(input("Ultimo digito de la placa del carro: "))
    if color == 1 or color == 2:
        amarillo = amarillo + 1
        
    elif color == 3 or color == 4:
        rosa = rosa + 1
        
    elif color == 5 or color == 6:
        rojo = rojo + 1
        
    elif color == 7 or color == 8:
        verde = verde + 1
        
        
    elif color == 9 or color == 0:
        azul = azul + 1
        
    else:
        print("Escriba un numero valido")
        
print("Carros con calcomania rosa: ",rosa)
print("Carros con calcomania amarilla: ",amarillo)
print("Carros con calcomania rojo: ",rojo)
print("Carros con calcomania verde: ",verde)
print("Carros con calcomania azul: ",azul)
print("")

