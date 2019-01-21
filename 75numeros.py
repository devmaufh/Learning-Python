print ("Dado un grupo de 75 Numeros (Diferentes a Cero), realice un algoritmo que permita determinar y dar como salida lo siguiente")
print ("Numero mayor y numero menor")
print ("Cantidad de numeros negativos")
print ("Numeros mayores a 150")
print "promedio de los numeros positivos"
mayor=0
menor=None
negative_counter=0
Highers150=0
avg=0.0
for x in xrange(1,15+1):
	number=int(raw_input("Numero %i " %x))
	if(menor==None):
		menor=number
	elif number<menor:
		menor=number
	if number>mayor:
		mayor=number
	if number<0:
		negative_counter=negative_counter+1
	elif number>=0:
		if number>150:
			Highers150=Highers150+1
		avg=avg+number
avg=avg/15

print ("Numero mayor: %i" %mayor)
print ("Numero menor: %i"%menor)
print ("Cantidad de numeros negativos: %i"%negative_counter)
print ("Numeros mayores a 150: %i"%Highers150)
print ("Promedio de numeros positivos: %i"%avg)
 