def main():
    # escribe tu código abajo de esta línea
    JN = int(input("Dame la cantidad de juegos nuevos: "))
    JU = int(input("Dame la cantidad de juegos usados: "))

    total = (JN*1000) + (JU*350) 
    print("El total de la compra es:", total)


if __name__ == '__main__':
    main()
