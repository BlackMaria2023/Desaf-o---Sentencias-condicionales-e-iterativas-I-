import math

#variables solicitud datos

peso = int(input("ingrese un peso en Kg: "))
altura = int(input("ingrese una altura en cms: "))

#calculo proceso

IMC = peso/((altura/100)*(altura/100))

#resultado en la consola

print (f"Su IMC es: {IMC:.2f}")


if IMC < 18.5:
    print ( "La clasificación OMS es Bajo Peso")

elif IMC <= 25:
    print ("La clasificación OMS es Adecuado")

elif IMC <= 30: 
    print("La clasificación OMS es Sobrepeso")

elif IMC <= 35: 
    print("La clasificación OMS es Obesidad Grado I")

elif IMC <= 40: 
    print("La clasificación OMS es Obesidad Grado II")

elif IMC > 40:
    print("La clasificación OMS es Obesidad Grado III")    


