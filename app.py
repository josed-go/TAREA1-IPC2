from lista_doble import lista_doble
from persona import persona

persona1 = persona(1, "José G", 19)
persona2 = persona(2, "Leonel L", 35)
persona3 = persona(3, "Luis E", 21)
persona4 = persona(4, "Erick Bran", 27)
persona5 = persona(4, "Aang", 7)
persona6 = persona(4, "Lolo", 47)

lista_doble = lista_doble()

print("")

lista_doble.insertar_por_edad(persona1)
lista_doble.insertar_por_edad(persona2)
lista_doble.insertar_por_edad(persona3)
lista_doble.insertar_por_edad(persona4)
lista_doble.insertar_por_edad(persona5)
lista_doble.insertar_por_edad(persona6)


lista_doble.imprimir()
print("")