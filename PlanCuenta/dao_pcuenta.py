import sys
from Conexion.Conexion import Conector


class DaoPlanCuenta(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id_pcuenta, Codigo,Grupo,Descripcion,Naturaleza,Estado from plancuenta where Descripcion like '%" + str(buscar) + "%' "
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, pcuenta):
        correcto = True
        try:
            sql = "insert into plancuenta (Codigo,Grupo,Descripcion,Naturaleza,Estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (pcuenta.Codigo,pcuenta.grupo,pcuenta.descripcion,pcuenta.naturaleza,pcuenta.Estado))
            self.conn.commit()
        except Exception as e:
            print("Error al ingresar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, pcuenta):
        correcto = True
        try:
            sql = "update plancuenta set Codigo = %s, Grupo=%s,Descripcion=%s,Naturaleza=%s,Estado=%s where id_pcuenta = %s"
            self.conectar()
            self.conector.execute(sql, (pcuenta.Codigo,pcuenta.grupo,pcuenta.descripcion,pcuenta.naturaleza,pcuenta.Estado,pcuenta.idpcuenta))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eiminar(self, pcuenta):
        correcto = True
        try:
            sql = "delete from plancuenta where id_pcuenta = %s"
            self.conectar()
            self.conector.execute(sql, int(pcuenta.idpcuenta))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

