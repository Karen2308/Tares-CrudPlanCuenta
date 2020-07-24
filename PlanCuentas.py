from funciones import menu
from Grupo import int_grupo
from PlanCuenta import int_pcuenta
opc = ''
while True:
    opc = str(menu(['Grupos de Cuentas', 'Plan de Cuentas', 'Salir'],
                   'Menu Principal'))
    if opc == '1':
        int_grupo.ejecutar_grupo()
    elif opc == '2':
        int_pcuenta.ejecutar_Pcuenta()
    elif opc == '3':
        break
