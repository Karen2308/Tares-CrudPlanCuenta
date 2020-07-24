from Grupo.dao_grupo import DaoGrupo


class CtrGrupo:
    def __init__(self, grup=None):
        self.grupo = grup

    def consulta(self, buscar):
        objDao = DaoGrupo()
        return objDao.consultar(buscar)

    def ingresar(self, grup):
        objDao = DaoGrupo()
        return objDao.ingresar(grup)

    def modificar(self, grup):
        objDao = DaoGrupo()
        return objDao.modificar(grup)

    def eliminar(self, grup):
        objDao = DaoGrupo()
        return objDao.eiminar(grup)
