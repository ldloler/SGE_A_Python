print("Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.")

# Variable per contar les iteracions i per guardar la suma
cont = 0
suma = 0

while cont < 100:
    cont += 1
    suma += cont
    # print(f"cont: {cont} \nsum: {suma}") # Comprovar que sumen els numeros que toca.

print(f"La suma dels numeros entre 0 i 100 es: {suma}")