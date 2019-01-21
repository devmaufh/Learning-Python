class Player(object):
    def __init__(self,health,position, speed):
        self.health=health
        self.position=position
        self.speed=speed
    def set_attack(self, damage):
        self.health-=damage
        if self.health==0 | self.health<0:
            print("¡Danger!")    
    def move(self, direction):
        self.position=direction+" "+str(self.speed)
    def __str__(self):
        return "Health: "+str(self.health)

class Fighter(Player):
    def __init__(self, health, position,speed, damage):
        self.health=health
        self.position=position
        self.speed=speed
        self.damage=damage
    def atack(self,player):
        print("Attacking")
        player.set_attack(self.damage)

if __name__ == "__main__":
    fighter1=Fighter(100,"Left",50,66)
    fighter2=Fighter(100,"Right",40,9)
    print("Player 1",fighter1)
    print("Player 2",fighter2)
    fighter1.atack(fighter2)
    fighter2.atack(fighter1)
    print("Player 1",fighter1)
    print("Player 2",fighter2)


