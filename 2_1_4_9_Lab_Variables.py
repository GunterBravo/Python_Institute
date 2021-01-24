#Escenario
#Millas y kilómetros son unidades de longitud o distancia.

#Teniendo en mente que 1 equivale aproximadamente a 1.61 kilómetros, complemente el programa en el editor para que convierta de:

#Millas a kilómetros.
#Kilómetros a millas.

kilometros = float(input("Ingresa longitud en Kilometros: "))
millas = float(input("Ingresa longitud en Kilometros: "))

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")


