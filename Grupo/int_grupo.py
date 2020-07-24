from Grupo.ctr_grupo import CtrGrupo
from Grupo.mod_grupo import ModGrupo
import os

from funciones import menu

ctr = CtrGrupo()


def insertar(rango):
    for i in range(int(rango)):
        while True:
            descripcion = input("Ingrese la descripcion: ")
            if descripcion.strip() != '':
                break
            else:
                print('No ingreso ni un valor')
        cli = ModGrupo(descripcion=descripcion)
        if ctr.ingresar(cli):
            print("Registro grabado correctamente")
        else:
            print("Error al grabar el registro")


def modificar():
    while True:
        codigo = input("Ingrese la codigo a modificar: ")
        if codigo.strip() != '':
            break
        else:
            print('No ingreso ni un valor')
    while True:
        descripcion = input("Ingrese la descripcion: ")
        if descripcion.strip() != '':
            break
        else:
            print('No ingreso ni un valor')
    cli = ModGrupo(idgrupo=codigo, descripcion=descripcion)
    if ctr.modificar(cli):
        print("Registro modificado correctamente")
    else:
        print("Error al modificar el registro")


def consultar():
    buscar = input("Ingrese nombre a buscar: ")
    cli = ctr.consulta(buscar)
    print(" Codigo   Descripcion")
    for gru in cli:
        print('{:2}        {}'.format(gru[0], gru[1]))


def eliminar():
    codi = input("-Ingrese codigo: ")
    cli = ModGrupo(idgrupo=codi)
    if ctr.eliminar(cli):
        print("Registro eliminado correctamente")
    else:
        print("Error al eliminar el registro")


def ejecutar_grupo():
    opc = ''
    while True:
        opc = str(menu(['Ingresar', 'Consultar', 'Modificar', 'Eliminar', 'Retornar Menu Principal'],
                       'Menu Grupo de Cuentas'))
        if opc == '1':
            print('\n<<Insertar Datos>>')
            while True:
                valor = input('-Ingrese cantidad de datos a Ingresar')
                if len(str(valor).strip()) > 0 and int(valor) > 0:
                    insertar(valor)
                    break
                else:
                    print('<<Ingresar un numero mayor a 0>>')

        elif opc == '2':
            print('\n<<Insertar Datos>>')
            consultar()
            input('Presiona enter para continuar')
        elif opc == '3':
            print('\n<<Insertar Datos>>')
            modificar()
        elif opc == '4':
            print('\n<<Insertar Datos>>')
            eliminar()
        elif opc == '5':
            break
            os.system('cls')
