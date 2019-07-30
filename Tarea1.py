class Nodo:
    def __init__(self, nombre=None, edad=None, sig=None):
        self.nombre = nombre
        self.edad = edad
        self.sig = sig
    
    def __str__(self):
        return "%s %s" %(self.nombre, self.edad)

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar(self, dato):
        if self.cabeza == None:
            self.cabeza = dato

        if self.cola != None:
            self.cola.sig = dato

        self.cola = dato
    
    def modificar(self, dato, datoModificar):
        aux = self.cabeza
        anterior = aux
        while aux != None:
            if str(aux) == str(dato):
                print("Dato Encontrado y Modificado")
                datoModificar.sig = aux.sig
                anterior.sig = datoModificar
                return True
            anterior = aux
            aux = aux.sig
    
    def eliminar(self, dato):
        aux = self.cabeza
        anterior = aux
        while aux != None:
            if str(aux.sig) == str(dato):
                print("Dato Encontrado y Eliminado")
                anterior.sig = nodo.sig
                return True
            anterior = aux
            aux = aux.sig


    def listar(self):
        aux = self.cabeza
        while aux != None:
            print("%s %s" %(aux, "=>"))
            aux = aux.sig

if __name__ == "__main__":
    ls = ListaSimple()
    while(True):
        print("---Menu--\n"+
            "1. Agregar\n"+
            "2. Modificar\n"+
            "3. Eliminar\n"+
            "4. Imprimir")
        num = input("Ingrese su opcion: ")
        if num == "1":
            nombre = input("Ingrese un nombre: ")
            edad = input("Ingrese una edad: ")
            nod = Nodo(nombre, edad)
            ls.agregar(nod)
        if num == "2":
            print("Ingrese el nombre y edad del nodo a Modificar")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            nombreM = input("Nombre a Modificar: ")
            edadM = input("Edad a Modificar: ")
            nodE = Nodo(nombre, edad)
            nodEM = Nodo(nombreM, edadM)
            ls.modificar(nodE, nodEM)
        if num == "3":
            print("Ingrese el nombre y edad del nodo a Eliminar")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            nod = Nodo(nombre, edad)
            ls.eliminar(nod)
        if num == "4":
            ls.listar()

