import csv   
#Trabajando con archivos ***csv***
print "+---------------------------------------------------------+"
print "|         *** MANRIQUE MARTINEZ VERONICA  ***             |"    
print "+---------------------------------------------------------+"
print " _________________________________________________________"
print "|                         OPCIONES                        |"       
print "a) Leer                                                   |"
print "b) Insertar                                               |"                                             
print "c) Salir                                                  |"
print "|_________________________________________________________|"       
opcion = raw_input("ELIJA UNA OPCION: ")

if opcion == "a" :
    print "El archivo tiene los siguientes registros:  "
    with open ('data.csv','r') as file:  
        data=csv.reader (file,delimiter='|')
        for line in data:
            print line

if opcion == 'b':
    print "Incerta un nuevo registro"
    nombre=raw_input("Escribe el nombre:   ")
    email=raw_input("Escribe el email:   ")
    with open ('data.csv','a')as file:
        data = csv.writer(file,delimiter='|')
        data.writerow([nombre,email])

        print "Hay un nuevo registro...Revise su informacion "
if opcion == 'c':
    print "Usted a decidido salir del sistema"
