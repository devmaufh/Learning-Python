print ":::::::::::::Practica if"
nombre="arturo"
if nombre=="Mario":
	print "Hola Mario"
else:
	print "Hola arturo"
print "_____________FIn IF" 
print ":::::::::::::Practica While"
contador=0
while contador<5:
	print "Numero: %i" % contador
	contador=contador+1
print "_____________FIn while" 
print ":::::::::::::Practica FOR"
for x in xrange(5,10):
	print "for1: %i"%x
print "_____________For 2: "
for x in xrange(1,100,25):
	print "for2 %i"%x
for c in "Ciclo for":
	print "Letra: %s" %c
print "Fin for"