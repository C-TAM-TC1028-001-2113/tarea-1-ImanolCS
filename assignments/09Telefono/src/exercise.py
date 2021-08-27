def main():
    # escribe tu código abajo de esta línea
    mens= int(input("Dame el numero de mensajes: "))
    megas= float(input("Dame el numero de megas: "))
    min= int(input("Dame el numero de minutos: "))

    
    costo =  (mens + megas + min)*0.8
    round(costo, 2)
    print("El costo mensual es:", costo)

if __name__ == '__main__':
    main()
