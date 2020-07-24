from Grupo.ctr_grupo import CtrGrupo
from PlanCuenta.ctr_pcuenta import CtrPcuenta
from PlanCuenta.mod_pcuenta import ModPlanCuenta
import os

from funciones import menu

ctr = CtrPcuenta()
ctrgrupo = CtrGrupo()
buscar = ""


def insertar(rango):
    for i in range(int(rango)):
        while True:
            codigo = input("Ingrese la codigo: ")
            if str(codigo).strip() != '':
                break
            else:
                print('No ingreso ni un valor')
        bandera = True
        while bandera:
            print("\nGrupos Existentes")
            cli = ctrgrupo.consulta(buscar)
            print(" Codigo   Descripcion")
            for gru in cli:
                print('{:2}        {}'.format(gru[0], gru[1]))
            while True:
                grupo = input("Ingrese el codigo de grupo: ")
                if grupo.strip() != '':
                    break
                else:
                    print('No ingreso ni un valor')
            for val in cli:
                if val[0] == int(grupo):
                    bandera = False
            if bandera == True:
                print("\n<<El codigo de grupo no existe>>")
        while True:
            descripcion = input("Ingrese la descripcion: ")
            if descripcion.strip() != '':
                break
            else:
                print('No ingreso ni un valor')
        ban = True
        while ban:
            print("\nLa naturaleza debe ser D=Deudora o A=Acreedora")
            while True:
                naturaleza = input("Ingrese la naturaleza: ")
                if naturaleza.strip() != '':
                    break
                else:
                    print('No ingreso ni un valor')
            if naturaleza == 'D' or naturaleza == 'A':
                ban = False
                break
            else:
                print("\n<<Dato ingresado incorrectamente>>")
        bane = True
        while bane:
            print("\nEl Estado debe ser True=Activo o False=Inactivo")
            while True:
                Estado = input("Ingrese la estado: ")
                if Estado.strip() != '':
                    break
                else:
                    print('No ingreso ni un valor')
            if Estado == 'True' or Estado == 'False':
                estado = 1 if Estado == 'True' else 0
                bane = False
            else:
                print("\n<<Dato ingresado incorrectamente>>")

        cli = ModPlanCuenta(Codigo=codigo, grupo=grupo, descripcion=descripcion, naturaleza=naturaleza, Estado=estado)
        if ctr.ingresar(cli):
            print("Registro grabado correctamente")
        else:
            print("Error al grabar el registro")


def modificar():
    while True:
        idpcuenta = input("Ingrese el Codigo a Modificar")
        if idpcuenta.strip() != '':
            break;

    while True:
        codigo = input("Ingrese la codigo: ")
        if str(codigo).strip() != '':
            break
        else:
            print('No ingreso ni un valor')
    bandera = True
    while bandera:
        print("\nGrupos Existentes")
        cli = ctrgrupo.consulta(buscar)
        print(" Codigo   Descripcion")
        for gru in cli:
            print('{:2}        {}'.format(gru[0], gru[1]))
        while True:
            grupo = input("Ingrese el codigo de grupo: ")
            if grupo.strip() != '':
                break
            else:
                print('No ingreso ni un valor')
        for val in cli:
            if val[0] == int(grupo):
                bandera = False
        if bandera == True:
            print("\n<<El codigo de grupo no existe>>")
    while True:
        descripcion = input("Ingrese la descripcion: ")
        if descripcion.strip() != '':
            break
        else:
            print('No ingreso ni un valor')
    ban = True
    while ban:
        print("\nLa naturaleza debe ser D=Deudora o A=Acreedora")
        while True:
            naturaleza = input("Ingrese la naturaleza: ")
            if naturaleza.strip() != '':
                break
            else:
                print('No ingreso ni un valor')
        if naturaleza == 'D' or naturaleza == 'A':
            ban = False
            break
        else:
            print("\n<<Dato ingresado incorrectamente>>")
    bane = True
    while bane:
        print("\nEl Estado debe ser True=Activo o False=Inactivo")
        while True:
            Estado = input("Ingrese la estado: ")
            if Estado.strip() != '':
                break
            else:
                print('No ingreso ni un valor')
        if Estado == 'True' or Estado == 'False':
            estado = 1 if Estado == 'True' else 0
            bane = False
        else:
            print("\n<<Dato ingresado incorrectamente>>")
    cli = ModPlanCuenta(idpcuenta=idpcuenta, Codigo=codigo, grupo=grupo, descripcion=descripcion, naturaleza=naturaleza,
                        Estado=estado)
    if ctr.modificar(cli):
        print("Registro modificado correctamente")
    else:
        print("Error al modificar el registro")


def consultar():
    buscar = input("Ingrese nombre a buscar: ")
    cli = ctr.consulta(buscar)
    print(" Id   Codigo   Grupo   Descripcion   Naturaleza   Estado")
    for gru in cli:
        print('{:2}    {:7}{:3}       {:14}{:13}{}'.format(gru[0], gru[1], gru[2], gru[3], gru[4], (
            "True" if int.from_bytes(gru[5], byteorder='big') == 1 else "False")))


def eliminar():
    codi = input("-Ingrese codigo: ")
    cli = ModPlanCuenta(idpcuenta=codi)
    if ctr.eliminar(cli):
        print("Registro eliminado correctamente")
    else:
        print("Error al eliminar el registro")


def ejecutar_Pcuenta():
    opc = ''
    while True:
        opc = str(menu(['Ingresar', 'Consultar', 'Modificar', 'Eliminar', 'Retornar Menu Principal'],
                       'Menu Grupo de Cuentas'))
        if opc == '1':
            print('\n<<Insertar Datos>>')
            while True:
                valor = input('-Ingrese cantidad de datos a Ingresar')
                if len(str(valor).strip()) > 0 and int(valor) >0:
                    insertar(valor)
                    break
                else:
                    print('<<Ingresar un numero mayor a 0>>')
        elif opc == '2':
            print('\n<<Insertar Datos>>')
            consultar()
        elif opc == '3':
            print('\n<<Insertar Datos>>')
            modificar()
        elif opc == '4':
            print('\n<<Insertar Datos>>')
            eliminar()
        elif opc == '5':
            break
            os.system('cls')
