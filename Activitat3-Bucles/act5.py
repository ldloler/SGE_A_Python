print("Sumar els números parells i els imparells continguts en la següent llista. Utilitzar for: ")

# Llista de numeros
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

# Variables de suma
sumParells = 0
sumImparells = 0

for i in num:
    if i % 2 == 0:
        sumParells += i
    else:
        sumImparells += i

print(f"Suma parells: {sumParells}")
print(f"Suma Imparells: {sumImparells}")