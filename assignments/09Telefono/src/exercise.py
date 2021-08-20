def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    pass
print ('Dame el número de mensajes:')
mensajes= int(input())
print ('Dame el número de megas:')
megas= float(input())
print ('Dame el número de minutos:')
minutos= int(input())

Costo=(mensajes*0.80)+(megas*0.80)+(minutos*0.80)
print ('El costo mensual es:')
print(Costo)


if __name__ == '__main__':
    main()
