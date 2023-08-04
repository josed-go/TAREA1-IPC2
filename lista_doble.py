from nodo import nodo

class lista_doble:
    def __init__(self):
        self.primero = None

    def insertar_por_edad(self, persona):
        nuevo_nodo = nodo(persona = persona)
        if self.primero is None:
            self.primero = nuevo_nodo
            return
        if persona.edad < self.primero.persona.edad:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
            return

        actual = self.primero

        while actual.siguiente and actual.siguiente.persona.edad < persona.edad:
            actual = actual.siguiente

        nuevo_nodo.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = nuevo_nodo
        
        actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = actual

    def imprimir(self):
        if self.primero is None:
            print("La lista esta vacia")
            return
        
        actual = self.primero

        print("ID: ", actual.persona.id, "|",
              "Nombre: ", actual.persona.nombre, "|",
              "Edad: ", actual.persona.edad)
        
        while actual.siguiente:
            actual = actual.siguiente

            print("ID: ", actual.persona.id, "|",
              "Nombre: ", actual.persona.nombre, "|" ,
              "Edad: ", actual.persona.edad)