#Este programa almacenara informacion de las reservas de una empresa dedicada
    
class Persona:
    # Aqui iran los atributos de la clase Persona
    def _init_(self, Nombre, Edad):
        self.Nombre=str(Nombre)
        self.Edad=int(Edad)

class Empleado: 
    #Aqui iran los atributos de la clase Empleado
    def _init_(self, Nombre, SueldoBruto):
        self.Nombre=str(Nombre)
        self.SueldoBruto=int(SueldoBruto)
        
class Cliente: 
    #Aqui iran los atributos de la clase Cliente
    def _init_(self, Nombre, TelefonoContacto):
        self.Nombre=str(Nombre)
        self. TelefonoContacto=int(TelefonoContacto)
        
class Directivo:
    #Aqui iran los atributos y funciones de la clase Directivo
    def _init_(self, Categoria, Subordinados):
        self.Categoria= str(Categoria)
        self.Subordinados=int(Subordinados)
    
    def Agregar_subordinado(Empleado):
        Agregar_subordinado= Empleado.Nombre - Empleado.Edad
        
    def Quitar_subordinado(Empleado):
        Quitar_subordinado= Empleado.Nombre - Empleado.Edad
        
class Empresa:
    #Aqui iran los atributos y funciones de la clase Empresa
    def _init_(self, Nombre, Empleados, Clientes):
        self.Nombre= str(Nombre)
        self.Empleados=int(Empleados)
        self.Clientes=int(Clientes)
    
    def Agregar_Empleado():
        Agregar_Empleado= Empleado.Nombre 
        
    def Quitar_Empleado():
        Quitar_Empleado= Empleado.Nombre
    
    def Agregar_Cliente():
        Agregar_Cliente= Cliente.Nombre 
        
    def Quitar_Cliente():
        Quitar_Cliente= Cliente.Nombre