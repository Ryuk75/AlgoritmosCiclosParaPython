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

#2. Un Zoólogo pretende determinar el porcentaje de animales que hay en las
#siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
#de 3 o mas años. El zoológico todavía no está seguro del animal que va
#estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
#si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará 40.
print("2/ Determinar el porcentaje de animales que hay en categorias de edades:")
porcentaje0_1 = 0
porcentaje1_2 = 0
porcentaje3 = 0

print("Escoja el animal a estudiar: \n"
      "1. Elefante \n"
      "2. Jirafa \n"
      "3. Chimpance")
estudio = int(input(":"))
if estudio == 1:
    print("Se escogio elefante")
    cantidad = 20
    for i in range(cantidad):
        edad = int(input("Ingrese la edad de la Elefante: "))
        if edad >= 0 and edad <= 1:
            porcentaje0_1 += 1
        elif edad == 2:
            porcentaje1_2 += 1
        elif edad >= 3:
            porcentaje3 += 1
if estudio == 2:
    print("Se escogio jirafa")
    cantidad = 15
    for i in range(cantidad):
        edad = int(input("Ingrese la edad de la Jirafa: "))
        if edad >= 0 and edad <= 1:
            porcentaje0_1 += 1
        elif edad == 2:
            porcentaje1_2 += 1
        elif edad >= 3:
            porcentaje3 += 1
if estudio == 3:
    print("Se escogio Chimpance")
    cantidad = 40
    for i in range(cantidad):
        edad = int(input("Ingrese la edad de el Chimpance: "))
        if edad >= 0 and edad <= 1:
            porcentaje0_1 += 1
        elif edad == 2:
            porcentaje1_2 += 1
        elif edad >= 3:
            porcentaje3 += 1
else: 
    print("Escoja un número válido")
    
porcentaje0_1 = (porcentaje0_1*100)/cantidad
porcentaje1_2 = (porcentaje1_2*100)/cantidad
porcentaje3 = (porcentaje3*100)/cantidad

print("Porcentajes de las edades de el animal que se escogió: ")
print("Porcentaje en la edad de 0 a 1 años es: ",porcentaje0_1)
print("Porcentaje en la edad de 1 a 2 años es: ",porcentaje1_2)
print("Porcentaje en la edad de 3 o más años: ",porcentaje3)
print("")
