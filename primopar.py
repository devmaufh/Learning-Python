print "Identifica numeros primos y pares"
n=int(raw_input("Ingresa un numero: "))
counter=0
for x in xrange(1,n+1):
	print x
	if n%x==0:
		counter=counter+1
if counter!=2:
	print "No primo"
else:
	print "Es primo"