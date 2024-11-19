# Variable de la nota
nota = float(input("Introdueix la nota de l'alumne: "))

# La nota es menys de 5? Suspes
if nota < 5:
    print("L'alumne ha Suspès")
# La nota es entre 5 i 6,5? Aprovat
elif nota >= 5 and nota <= 6.5:
    print("L'alumne ha Aprovat")
# La nota es major a 8? Exelent
elif nota > 8:
    print("L'alumne te un Exelent")
# Es alguna altre cosa? Es un notable. (L'unica comprobació que queda es: que la nota sigui mes de un 6.5 fins un 8)
else:
    print("L'alumne te un Notable")