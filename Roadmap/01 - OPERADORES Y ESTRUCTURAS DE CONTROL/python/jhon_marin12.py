x = 12.1
y = 3

# Operadores Aritmeticos

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
division_entera = x // y
modulo = x % y
potenciacion = x ** y

#Las strings soportan una especie de operaciones
nombre_completo = 'Jhon' + 'Marin'
mult_string = 'hola' * 3


# Operadores de comparacion
# En python estos retornan un valor booleeano

equals = 5 == 4
no_igual = 5 != 5
es_menor = 3 < 5
es_menor_igual = 3 <= 5
es_mayor = 6 > 9
es_mayor_igual =6 >= 5

#Operadores logicos
#Se pueden complementar con los operadores de comparacion
#Recordar algebra booleana

a = 6 > 5 and 5 > 3 #Se tienen que cumplir todas las comparaciones para obtener True
b = 6 > 5 or 5 > 3 #Se debe cumplir al menos una para que retorne True
c = not(4 == 4) # invierte por asi decirlo, el resultado de la operacion que tenga dentro


#Estructuras de control

#if - elif - else
x = 10
if x > 0:
    print("Es un numero positivo")
elif x < 0:
    print("Es un numero negativo")
else:
    print("El numero es 0")

# while y for

while x > 0:
    print(x)
    x -=1
else:
    print("Salimos del bucle while")


for i in range(101):
    if i%2 == 0:
        print("el numero {} es par".format(i))
    else:
        print("el numero {} es impar".format(i))


# Ejercicio Extra
for i in range(10,56): #Debemos sumar 1 al numero para tomarlo
    if i%2 == 0 and i != 16 and i%3 != 0:
        print(i)
