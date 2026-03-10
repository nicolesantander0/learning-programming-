class Pila:
    def __init__(self, *args):
        # Se aceptan argumentos para inicializar la pila con datos
        self.items = list(args)

    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        # Se elimina la condición 'if' y se pasa el 'item' correctamente
        self.items.append(item)
    
    def desapilar(self):
        if self.esta_vacia():
             return "La pila está vacía"
        return self.items.pop()
    
# Ejemplo (manteniendo tu código original)
navegacion = Pila("juanjo", "obando")
navegacion.apilar("Pagina inicio")
navegacion.apilar("Articulo de python")
navegacion.apilar("Seccion comentarios")

print(f"saliendo de: {navegacion.desapilar()}")