class Persona:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.pesoPersona = peso
    
    def agregarCabina(self, nroCab):
        pass

class Cabina:
    def __init__(self, nroCabina):
        self.nroCabina = nroCabina
        self.personasAbordo = []
    
    def agregarPersona(self, persona):
        self.personasAbordo.append(persona)
    
    def calcularPesoTotal(self):
        peso_total = 0
        for persona in self.personasAbordo:
            peso_total += persona.pesoPersona
        return peso_total
    
    def verificarReglas(self):
        if len(self.personasAbordo) > 10:
            return False
        if self.calcularPesoTotal() > 850:
            return False
        return True

class Linea:
    def __init__(self, color):
        self.color = color
        self.filaPersonas = []
        self.cabinas = []
        self.cantidadCabinas = 0
        self.ingresos = 0
    
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
            
            if persona.edad <= 25 or persona.edad >= 60:
                self.ingresos += 1.5
            else:
                self.ingresos += 3.0
                
            return True
        else:
            print("No se puede agregar persona: límite excedido")
            return False
    
    def verificarReglasLinea(self):
        for cabina in self.cabinas:
            if not cabina.verificarReglas():
                return False
        return True
    
    def calcularIngresos(self):
        return self.ingresos
    
    def calcularIngresosRegulares(self):
        ingresos_regulares = 0
        for cabina in self.cabinas:
            for persona in cabina.personasAbordo:
                if persona.edad > 25 and persona.edad < 60:
                    ingresos_regulares += 3.0
        return ingresos_regulares

class MiTeleferico:
    def __init__(self):
        self.lineas = []
        self.cantidadIngresos = 0
    
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
                nro_cabina = linea.cantidadCabinas + 1
                return linea.agregarCabina(nro_cabina)
        print(f"No existe la línea {linea_color}")
        return None
    
    def agregarPrimeraPersonaCabina(self, nroX, linea_color):
        for linea in self.lineas:
            if linea.color == linea_color:
                return linea.agregarPrimeraPersonaCabina(nroX)
        print(f"No existe la línea {linea_color}")
        return False
    
    def verificarTodasCabinas(self):
        for linea in self.lineas:
            if not linea.verificarReglasLinea():
                return False
        return True
    
    def calcularIngresoTotal(self):
        total = 0
        for linea in self.lineas:
            total += linea.calcularIngresos()
        self.cantidadIngresos = total
        return total
    
    def lineaMasIngresoRegular(self):
        if not self.lineas:
            return None
        
        linea_mayor = self.lineas[0]
        mayor_ingreso = linea_mayor.calcularIngresosRegulares()
        
        for linea in self.lineas[1:]:
            ingreso_actual = linea.calcularIngresosRegulares()
            if ingreso_actual > mayor_ingreso:
                mayor_ingreso = ingreso_actual
                linea_mayor = linea
        
        return linea_mayor

def main():
    teleferico = MiTeleferico()
    
    linea_amarilla = Linea("Amarillo")
    linea_roja = Linea("Rojo")
    linea_verde = Linea("Verde")
    
    teleferico.agregarLinea(linea_amarilla)
    teleferico.agregarLinea(linea_roja)
    teleferico.agregarLinea(linea_verde)
    
    for i in range(3):
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
    if teleferico.verificarTodasCabinas():
        print("Todas las cabinas cumplen las reglas")
    else:
        print("Algunas cabinas no cumplen las reglas")
    
    print("\n=== Cálculo de ingresos ===")
    ingreso_total = teleferico.calcularIngresoTotal()
    print(f"Ingreso total: {ingreso_total} Bs")
    
    print("\n=== Línea con más ingreso regular ===")
    linea_mayor = teleferico.lineaMasIngresoRegular()
    if linea_mayor:
        ingreso_regular = linea_mayor.calcularIngresosRegulares()
        print(f"Línea {linea_mayor.color} tiene {ingreso_regular} Bs en tarifa regular")

if __name__ == "__main__":
    main()

