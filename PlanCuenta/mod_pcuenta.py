class ModPlanCuenta:
    def __init__(self, idpcuenta=0, Codigo='', grupo=0, descripcion='', naturaleza='', Estado=True):
        self.__idpcuenta = idpcuenta
        self.__Codigo = Codigo
        self.__grupo = grupo
        self.descripcion = descripcion
        self.naturaleza = naturaleza
        self.Estado = Estado

    @property
    def idpcuenta(self):
        return self.__idpcuenta

    @property
    def Codigo(self):
        return self.__Codigo

    @property
    def grupo(self):
        return self.__grupo
