class Persona:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.pesoPersona = peso


class Cabina:
    def __init__(self, nroCabina):
        self.nroCabina = nroCabina
        self.personasAbordo = []
    
    def agregarPersona(self, persona):
        self.personasAbordo.append(persona)
    
    def calcularPesoTotal(self):
        return sum(p.pesoPersona for p in self.personasAbordo)
    
    def verificarReglas(self):
        return len(self.personasAbordo) <= 10 and self.calcularPesoTotal() <= 850


class Linea:
    def __init__(self, color):
        self.color = color
        self.filaPersonas = []
        self.cabinas = []
        self.cantidadCabinas = 0
    
    def agregarPersona(self, persona):
        self.filaPersonas.append(persona)
    
    def agregarCabina(self, nroCabina):
        nueva_cabina = Cabina(nroCabina)
        self.cabinas.append(nueva_cabina)
        self.cantidadCabinas += 1
        return nueva_cabina
    
    def encontrarCabina(self, nroX):
        for cabina in self.cabinas:
            if cabina.nroCabina == nroX:
                return cabina
        return None
    
    # INCISO A
    def agregarPrimeraPersonaCabina(self, nroX):
        cabina = self.encontrarCabina(nroX)
        if cabina is None:
            print(f"No existe la cabina {nroX}")
            return False
        
        if len(self.filaPersonas) == 0:
            print("No hay personas en la fila")
            return False
        
        persona = self.filaPersonas[0]
        
        peso_actual = cabina.calcularPesoTotal()
        if len(cabina.personasAbordo) < 10 and (peso_actual + persona.pesoPersona) <= 850:
            cabina.agregarPersona(persona)
            self.filaPersonas.pop(0)
            return True
        else:
            print("No se puede agregar persona: límite excedido")
            return False
    
    # INCISO B
    def verificarReglasLinea(self):
        for cabina in self.cabinas:
            if not cabina.verificarReglas():
                return False
        return True
    
    # INCISO C
    def calcularIngresos(self):
        ingreso = 0
        for cabina in self.cabinas:
            for persona in cabina.personasAbordo:
                if persona.edad <= 25 or persona.edad >= 60:
                    ingreso += 1.5
                else:
                    ingreso += 3
        return ingreso
    
    # INCISO D (solo tarifa regular)
    def calcularIngresosRegulares(self):
        ingreso = 0
        for cabina in self.cabinas:
            for persona in cabina.personasAbordo:
                if 25 < persona.edad < 60:
                    ingreso += 3
        return ingreso


class MiTeleferico:
    def __init__(self):
        self.lineas = []
    
    def agregarLinea(self, linea):
        self.lineas.append(linea)
    
    def agregarPersonaFila(self, persona, linea_color):
        for linea in self.lineas:
            if linea.color == linea_color:
                linea.agregarPersona(persona)
                return True
        print(f"No existe la línea {linea_color}")
        return False
    
    def agregarCabina(self, linea_color):
        for linea in self.lineas:
            if linea.color == linea_color:
                nro = linea.cantidadCabinas + 1
                return linea.agregarCabina(nro)
        print(f"No existe la línea {linea_color}")
        return None
    
    def agregarPrimeraPersonaCabina(self, nroX, linea_color):
        for linea in self.lineas:
            if linea.color == linea_color:
                return linea.agregarPrimeraPersonaCabina(nroX)
        print(f"No existe la línea {linea_color}")
        return False
    
    def verificarTodasCabinas(self):
        return all(linea.verificarReglasLinea() for linea in self.lineas)
    
    def calcularIngresoTotal(self):
        return sum(linea.calcularIngresos() for linea in self.lineas)
    
    def lineaMasIngresoRegular(self):
        if not self.lineas:
            return None
        return max(self.lineas, key=lambda l: l.calcularIngresosRegulares())


def main():
    teleferico = MiTeleferico()
    
    linea_amarilla = Linea("Amarillo")
    linea_roja = Linea("Rojo")
    linea_verde = Linea("Verde")
    
    teleferico.agregarLinea(linea_amarilla)
    teleferico.agregarLinea(linea_roja)
    teleferico.agregarLinea(linea_verde)
    
    for _ in range(3):
        teleferico.agregarCabina("Amarillo")
        teleferico.agregarCabina("Rojo")
        teleferico.agregarCabina("Verde")
    
    personas = [
        Persona("Juan", 20, 65.5),
        Persona("Maria", 35, 58.0),
        Persona("Pedro", 70, 72.3),
        Persona("Ana", 28, 61.7),
        Persona("Luis", 45, 80.1),
        Persona("Carmen", 62, 55.8)
    ]
    
    for persona in personas:
        teleferico.agregarPersonaFila(persona, "Amarillo")
        teleferico.agregarPersonaFila(persona, "Rojo")
        teleferico.agregarPersonaFila(persona, "Verde")
    
    print("=== Agregando personas a cabinas ===")
    for i in range(1, 4):
        teleferico.agregarPrimeraPersonaCabina(i, "Amarillo")
        teleferico.agregarPrimeraPersonaCabina(i, "Rojo")
        teleferico.agregarPrimeraPersonaCabina(i, "Verde")
    
    print("\n=== Verificación de reglas ===")
    print("Todas las cabinas cumplen las reglas" if teleferico.verificarTodasCabinas() else "Hay cabinas que NO cumplen")
    
    print("\n=== Ingreso total ===")
    print(teleferico.calcularIngresoTotal(), "Bs")
    
    print("\n=== Línea con más ingreso regular ===")
    linea = teleferico.lineaMasIngresoRegular()
    if linea:
        print(f"Línea {linea.color} con {linea.calcularIngresosRegulares()} Bs")


if __name__ == "__main__":
    main()
