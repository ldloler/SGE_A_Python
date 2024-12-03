# Impotem les classes
from cotxe import cotxe
from colibri import colibri

# Creem 3 instancies de cotxe
cotxe1 = cotxe("Ford", "Mustang", 3, 5, "Gasolina")
cotxe2 = cotxe("Toyota", "Ralf 4", 5, 5, "Hybrid")
cotxe3 = cotxe("Ferrari", "La Ferrari", 3, 2, "Gasolina")

# Creem 3 instancies de colibri
colibri1 = colibri("Manel", "Verd i groc", "Montseny", "Necter", "Cap") 
colibri2 = colibri("Sara", "Blau i verd", "Montseny", "Necter", "Ala trencada")
colibri3 = colibri("Pol", "Vermell i groc", "Montseny", "Necter", "Cap")

# 3 getters de cotxe
print('\nPrint de 3 getters de cotxe:')
print(cotxe1.getMarca())
print(cotxe1.getModel())
print(cotxe1.getTipus())

# 4 getters de colibri
print('\nPrint de 4 getters de colibri:')
print(colibri2.getNom())
print(colibri2.getColor())
print(colibri2.getMalaltia())
print(colibri2.getLocalitzacio())

# Modifica 2 attributs de cotxe
cotxe2.setNumPortes(3)
cotxe2.setSeients(4)

# Mostra els 2 atributs modificats
print('\nPrint dels 2 atributs modificats:')
print(f'El nou numero de portes del cotxe2 es: {cotxe2.getNumPortes()}')
print(f'El nou numero de seients del cotxe2 es: {cotxe2.getSeients()}')

# Modifica 2 attributs de colibri
colibri3.setNom("Amelia")
colibri3.setColor("Lila i vermell")

# Mostra els 2 atributs modificats
print('\nPrint dels 2 atributs modificats:')
print(f'El nou nom de colibri3 es: {colibri3.getNom()}')
print(f'El nou color de colibri3 es: {colibri3.getColor()}')