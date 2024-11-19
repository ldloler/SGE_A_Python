print("Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: ")

# Llista de numeros
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

for i in num:
    if i % 2 == 0:
        print(f"El numero {i} és parell")
    else:
        print(f"El numero {i} és imparell")

print("\n\nT'ho mostrare ordenat:")
print("\nParells:")
for i in num:
    if i % 2 == 0:
        print(f"{i}")

print("\nImparells: ")
for i in num:
    if i % 2 == 1:
        print(f"{i}")