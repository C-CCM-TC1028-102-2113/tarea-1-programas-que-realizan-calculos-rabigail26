def main():
    #escribe tu código abajo de esta línea
    pass
print ("Dame el saldo del mes anterior")
mesanterior = float (input())
print ("Dame los ingresos")
ingresos = float (input())
print ("Dame los egresos:")
egresos = float(input())
print ("Dame el numero de cheques expedidos")
cheques = int(input())
saldo = (mesanterior + ingresos -egresos) 
intereses=(((saldo -(saldo *(0.075))) + (cheques *13)) )
round(intereses,2)
print ("El saldo final es:")
print (intereses)
if __name__ == '__main__':
    main()
