def main():
    # escribe tu código abajo de esta línea
    from math import ceil 
    pal=int(input("Dame el número de palabras: "))

    pal = ceil(pal/475) 
    precio = pal*60*(0.9) 

    print("El costo de la publicación es:", precio)



if __name__ == '__main__':
    main()
