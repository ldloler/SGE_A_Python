# for recorent una llista
    # fara que i recorri la llista num.
    # Tingues en compte que es igual si es un numero, una string o el que sigui.
# ------
# num = [1,2,3,4,5,6,"hola"]
# for i in num:
#     print(i)
# print("adeu")

# while
    # es com en java
    # Tenir en compte de no fer-l'ho infinit
# ------
# i = 0
# while i < 10:
#     i += 1
#     print(i)

# for amb un range. (comença, fins on, quant suma)
# Tingues en compte que la llista anira desede "comença" fins a ("fins on" - 1)
    # Exemple: (1,12,2)
    # La llista que crea es [1,3,5,7,9,11]
    # # Exemple: (0,12,2)
    # La llista que crea es [0,2,4,6,8,10,12]
# ------
# for i in range(-1,12,2):
#     print(i)
# print("chao")

# Com demanar informació
    # Amb "imput"
    # Si volem que sigui especificament una tipus de variable s'ha de "castegar".
    # per fer-ho posem "srt(queVolemCastegar)" o "int(queVolemCastegar)" o el tipus de variable que voldrem guardar.
# ------
# resposta = str(input("Escriu alguna cosa: "))
# print(resposta)