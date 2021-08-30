def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingreso= float(input("Dame los ingresos: "))
    egreso = float(input("Dame los egresos: "))
    cheques= int(input("Dame el número de cheques: "))

    saldoF= ((saldo + ingreso - egreso - (cheques*13)) * (92.5/100)) 


    print("El saldo final de la cuenta es:", saldoF)


if __name__ == '__main__':
    main()
