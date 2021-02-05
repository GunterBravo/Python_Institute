# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
userWord = input("Ingresa la palabra para comer la vocal: ")
userWord = userWord.upper()
for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)

    # Completa el cuerpo del ciclo for.