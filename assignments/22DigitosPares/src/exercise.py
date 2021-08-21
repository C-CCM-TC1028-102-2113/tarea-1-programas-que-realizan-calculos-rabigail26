def main():
    #escribe tu código abajo de esta línea
    pass

#Numeros pares
valores = int(input("Inserte los digitos"))
if valores <0 :
    print("¡Error!")
else:
    pares = 0
if valores % 2 == 0:
    pares += 1
    print(f"Ha escrito {pares} números pares y {valores - pares} números impares.")



if __name__ == '__main__':
    main()
