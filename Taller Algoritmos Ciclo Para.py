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

#3. Una empresa se requiere calcular el salario semanal de cada uno de los n
#obreros que laboran en ella. El salario se obtiene de la siguiente forma:
#a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
#b. Si trabaja mas de 40 horas se le paga $20 por cada una de las primeras 40 horas y $25 por cada hora extra.

print("3/ Determine el salario semanal de los obreros:")
horas = int(input("Cuantas horas trabajó el obrero: "))
if horas <= 40:
    pago = horas*20
    print("El trabajador trabajó ",horas," horas y se le pagará: ",pago)
else:
    horaextra = horas-40
    pago = 40*20 + (horaextra*25)
    print("El trabajador trabajó ",horas," horas y se le pagará: ",pago)
print("")

#4. Calcular el promedio de edades de hombres, mujeres y
#de todo un grupo de alumnos.
print(" 4/ Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.")
edadF = 0
edadM = 0
numeroF = 0
numeroM = 0
numeroAlumnos = int(input("El total de alumnos es: "))
for i in range(numeroAlumnos):
    print("Escoja sexo \n"
          "F o f para femenino \n"
          "M o m para Masculino \n")
    sexo = input(":")
    edad = int(input("Su edad es: "))
    if sexo == "f" or sexo == "F":
        edadF = edadF + edad
        numeroF += 1
    if sexo == "m" or sexo == "M":
        edadM = edadM + edad
        numeroM += 1
    else: 
        print("Digito invalido")

promedioF = edadF / numeroF
promedioM = edadM / numeroM
promTotal = (edadF + edadM)/numeroAlumnos
print("El promedio de edades en mujeres es: ",promedioF)
print("El promedio de edades en hombres es: ",promedioM)
print("El promedio de edades en total es: ",promTotal)
print("")

#5. Encontrar el menor valor de un conjunto de n números dados
print("5/ Encontrar el menor valor de un conjunto de n números dados")
numC = int(input("Digite cantidad de numeros: "))
num = []
for i in range(numC):
     num.append(int(input("Digite un numero: ")))
menor = num[0]
for i in range(numC):
    if num[i] < menor:
        menor = num[i]
print("\n")
print("El número más pequeño es: " + str(menor))
print("")

#6. Cinco miembros de un club contra la obesidad desean
#saber cuanto han bajado o subido de peso desde la última vez que se reunieron. Para esto se debe realizar un ritual
#de pesaje en donde cada uno se pesa en diez básculas distintas para así tener el promedio mas exacto de su
#peso. Si existe diferencia positiva entre este promedio de peso y el peso de la última vez que se reunieron,
#significa que subieron de peso. Pero si la diferencia
#es negativa, significa que bajaron. Lo que el problema requiere es que por cada persona se imprima un letrero que
#diga: “SUBIÓ” o “BAJÓ” y la cantidad de kilos que subió o bajó de peso.
print("6/ Determinar por cada persona si subio o bajo de peso")
basculas = 10
cont = 0
pesoConocido = int(input("Ingrese el peso de la ultima reunión: "))
for i in range(basculas):
    peso = int(input("Digite peso dado por la bascula: "))
    cont = cont + peso

promedioPeso = cont / basculas
diferencia = promedioPeso - pesoConocido

if diferencia > 0:
    print("Esta persona subió ",diferencia," kg")
else:
   print("Esta persona bajó ",diferencia," kg")
print("")

#7. En un supermercado una ama de casa pone en su carrito los artículos que va tomando de los estantes. La señora
#quiere asegurarse de que el cajero le cobre bien lo que ella ha comprado, por lo que cada vez que toma un articulo
#anota su precio junto con la cantidad de artículos
#iguales que ha tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo que irá gastando en los
#demás artículos, hasta que decide que ya tomó todo lo que
#necesitaba. Ayúdele a esta señora a obtener el total de su compra.
print("7/ Determine el total de la compra: ")
cont = 0
numProductos = int(input("Digite el numero de productos a comprar sin contar si se llevan varios del mismo: "))
for i in range(numProductos):
    num = int(input("Digite el numero de paquetes que se llevara de este producto: "))
    precio = int(input("Digite el precio del producto individualmente: "))
    valor = num*precio
    cont = cont + valor
    print("El valor total de este producto es: $", valor)
print("El total de la compra es: $",cont)
print("")