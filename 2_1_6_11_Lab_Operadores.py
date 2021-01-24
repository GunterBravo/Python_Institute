'''
Escenario
La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado debe ser mostrado en la consola.
Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

rueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.
'''
print('Programa para alquiler de Cancha Sintica')
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))


hora_acumulada = (hora + (dura+min)//60)%24
minuto_final = (dura+min)%60

print("La hora termina:", hora_acumulada, ":", minuto_final)


