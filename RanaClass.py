from AnimalClass import Animal
class Rana(Animal):
    def __init__(self, nombre, color, venenoso):
        # Llamando al constructor de la superclase
        super().__init__(nombre, especie="Anfibio")
        self.color = color
        self.venenoso = venenoso

    def hacer_sonido(self):
        return "croac!"
    
rana = Rana("Swimy", "Naranja","Sí")
print(rana.obtener_informacion())