def main():
    # escribe tu código abajo de esta línea
    
     #Se requieren 50 gramos de levadura para 1 kg. de harina si se utiliza para la base de una pizza.
     #Realiza
     #el cálculo de la levadura necesitada a partir de los gramos de harina que indique el usuario.
     h= float(input("Dame la harina en gramos: "))

     levadura = h*(50/1000)
     print("Necesitas estos gramos de levadura:", levadura )


if __name__ == '__main__':
    main()
