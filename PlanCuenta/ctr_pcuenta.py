from PlanCuenta.dao_pcuenta import DaoPlanCuenta
from PlanCuenta.mod_pcuenta import ModPlanCuenta


class CtrPcuenta:
    def __init__(self, grup=None):
        self.grupo = grup

    def consulta(self, buscar):
        objDao = DaoPlanCuenta()
        return objDao.consultar(buscar)

    def ingresar(self, pcuenta):
        objDao = DaoPlanCuenta()
        return objDao.ingresar(pcuenta)

    def modificar(self, pcuenta):
        objDao = DaoPlanCuenta()
        return objDao.modificar(pcuenta)

    def eliminar(self, pcuenta):
        objDao = DaoPlanCuenta()
        return objDao.eiminar(pcuenta)

