import sys
from Conexion.Conexion import Conector


class DaoGrupo(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id_grupo, descripcion from grupo where descripcion like '%" + str(buscar) + "%' "
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

    def ingresar(self, grup):
        correcto = True
        try:
            sql = "insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql, (str(grup.descripcion)))
            self.conn.commit()
        except Exception as e:
            print("Error al ingresar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, grup):
        correcto = True
        try:
            sql = "update grupo set descripcion = %s where id_grupo = %s"
            self.conectar()
            self.conector.execute(sql, (grup.descripcion, grup.idgrupo))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eiminar(self, grup):
        correcto = True
        try:
            sql = "delete from grupo where id_grupo = %s"
            self.conectar()
            self.conector.execute(sql, int(grup.idgrupo))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

