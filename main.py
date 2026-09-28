class Dispositivo:
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado


    def obtener_nombre(self):
        return self.nombre

    def obtener_estado(self):
        return self.estado

class FocoInteligente(Dispositivo):

    def __init__(self, nombre, estado, color_luz):
        super().__init__(nombre, estado)
        self.__color_luz = color_luz

    def obtener_color_luz(self):
        return   self.__color_luz

        
    def ejecutar(self):
        print(f"{self.obtener_nombre()}|foco habitacion encendido|con un color de luz : {self.obtener_color_luz()}")

class ParlanteInteligente(Dispositivo):

    def __init__(self, nombre, estado, volumen):
        super().__init__(nombre, estado)
        self.__volumen = volumen

    def obtener_volumen(self):
        return self.__volumen
       
    def ejecutar(self):
        print(f"{self.obtener_nombre()}|parlante encendido  reproduciendose con un volumen de : {self.obtener_volumen()}")


Foco = FocoInteligente("Foco", "apagado", "Blanco cálido")
Parlante1 = ParlanteInteligente("Parlante", "apagao", 80)

Foco.ejecutar()
Parlante1.ejecutar()