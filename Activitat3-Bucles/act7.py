print("Amb while indicar si el número guardat a una variable està entre 100 i 400.")

# Variable per contar les iteracions i la del numero a comparar.
cont = 100
num = int(input("Quin numero vols veure si esta entre el 100 i el 400?: "))

while num != cont and cont != 400:
    cont += 1

if num == cont:
    print("El numero que m'has dit esta entre el 100 i el 400")
else:
    print("El numero que m'has dit NO esta entre el 100 i el 400")