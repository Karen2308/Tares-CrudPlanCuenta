class ModGrupo:
    def __init__(self, idgrupo=0, descripcion=''):
        self.__idgrupo = idgrupo
        self.__descripcion = descripcion

    @property
    def idgrupo(self):
        return self.__idgrupo

    @property
    def descripcion(self):
        return self.__descripcion