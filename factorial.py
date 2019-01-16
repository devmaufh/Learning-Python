print "Ejercicio: Estructuras de control"
var=int(raw_input("Ingresa un numero entero: "))
factorial=1
for x in xrange(1,var+1):
	factorial=factorial*x
print factorial