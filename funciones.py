def menu(opciones, titulo):
    print('*' * 30)
    print(' '* 2,'{}'.format(titulo))
    print('*' * 30)
    for op in range(0, len(opciones)):
        print("{}) {}".format(op + 1, opciones[op]))
    opc = input("Elija Opcion [1...{}]: ".format(len(opciones)))
    return opc
