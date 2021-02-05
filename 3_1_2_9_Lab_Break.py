#Objetivos
#Familiarizar al estudiante con:
#
#Utilizar la instrucción break en los ciclos.
#Reflejar situaciones de la vida real en código de computadora.
#Escenario
#La instrucción break se usa para salir/terminar un ciclo.
#
#Diseña un programa que use un ciclo while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el ciclo con éxito". Debe imprimirse en la pantalla y el ciclo debe terminar.
#
#No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la declaración break.

palabra = input("Ingresa la palabra escondida: ")

while True: 
    if palabra == "chupacabra":
        print("¡Has dejado el ciclo con éxito.")
        break
    else:
        palabra = input("ingresa otra vez: ")

#else:
#    print("¡Has dejado el ciclo con éxito.")
