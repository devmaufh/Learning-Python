f= open("test1.txt","r")
a=0
for i in f:
    a+=int(i) 
f="Last 10 digits are: "
for i in range(10):
     f+=str(a)[i]
print (f)