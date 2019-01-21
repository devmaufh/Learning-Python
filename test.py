mydict={}
text="Hola mundo que onda que pez"
for char in text:
    if char in mydict.keys():
        mydict[char]+=1
        
    else: 
        mydict[char]=1

mydict.pop(" ",None)
print(mydict)



for i in range(10):
    print(i)



