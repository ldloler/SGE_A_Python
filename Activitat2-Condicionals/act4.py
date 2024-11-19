# Variable de salari
salari = int(input("Quin es el salari?: "))

# Si el salari és menor de 15.000, s’aplica un 0% d’IVA. 
if salari < 15000:
    iva = 0
# Si el salari és menor de 30.000 s’aplica un 10% de l’iva.
elif salari >= 15000 and salari < 30000:
    iva = 10
# Si el salari és menor a 60.000 s’aplica un IVA del 21%.
elif salari >= 30000 and salari < 60000:
    iva = 21
# Si es mes gran de 60.000 et demana diners
else:
    print("Crec que tens prous diners com per fer una donació :)")
    iva = 100

print("L'iva que s'aplica es del: ", iva,"%")
# Calcul del salari
print("-",salari * iva/100)