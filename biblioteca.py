# ==========================================
# PARTE 1 - CLASE LIBRO
# ==========================================

class Libro:

    # Constructor
    def __init__(self, titulo, autor, año):

        self.titulo = titulo
        self.autor = autor
        self.año = año

    # Método mostrar información
    def mostrarInformacion(self):

        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.año)
        print("------------------------")


# ==========================================
# OBJETOS LIBRO
# ==========================================

libro1 = Libro(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967
)

libro2 = Libro(
    "Don Quijote",
    "Miguel de Cervantes",
    1605
)

libro3 = Libro(
    "El Principito",
    "Antoine de Saint-Exupéry",
    1943
)

# Mostrar información
libro1.mostrarInformacion()
libro2.mostrarInformacion()
libro3.mostrarInformacion()