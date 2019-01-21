class Paper(object):
    
    def write(self,stringText):
        self.text=stringText
    
    def __str__(self):
        return self.text

class Pencil(object):
    def __init__(self,ink):
        self.ink=ink
    def write(self, text,paper):
        if self.ink>0:
            newText=""
            for i in text:
                if self.ink==0:
                    print("The ink is finished")
                    break
                else:
                    newText+=i
                    self.ink-=1
            paper.write(newText)
        else:
            print("The ink is finished")
        
    def __str__(self):
        return "Ink: "+str(self.ink)

class Marker(Pencil):
    def __init__(self, ink):
        self.ink=ink
    def recharge(self,quantity):
        self.ink=quantity

if __name__ == "__main__":
    p=Paper()
    marker=Marker(4)
    marker.write("Hola mundo",p)
    print(p)
    p2=Paper()
    marker.recharge(10)
    marker.write("Hola mundo",p2)
    print(p2)
