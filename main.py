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
        Auto.cantidadCreados+=1
    
    def cantidadAsientos(self):
        count=0
        for i in self.asientos:
            if i is not None:
                count+=1
        return count
    
    def verificarIntegridad(self):
        check=True
        for i in self.asientos:
            if i is not None:
                if self.registro!=i.registro:
                    check=False
        if (check and self.registro==self.motor.registro):
            return "Auto original"
        else:
            return "Las piezas no son originales"
    

class Motor:
    def __init__(self,numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if (tipo in["electrico","gasolina"]):
            self.tipo=tipo