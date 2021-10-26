class Asiento:
    def __init__(self,color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,color):
        if (color in ["rojo", "verde", "amarillo", "negro", "blanco"]):
            self.color=color
        
class Auto:
    cantidadCreados=0
    def __init__(self,modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        count=0
        for i in self.asientos:
            if i!=None:
                count+=1
    
    def verificarIntegridad(self):
        check=True
        for i in self.asientos:
            if i!=None:
                if self.registro!=i.registro:
                    check=False
        if (check and self.registro==self.motor.registro):
            return "Auto original"
        else:
            return "Las piezas no son originales"
    

class motor:
    def __init__(self,numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if (tipo in["electrico","gasolina"]):
            self.tipo=tipo