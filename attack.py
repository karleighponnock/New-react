import random 


class Enemy:
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
        

    def getAtk(self):
        print(self.atkl)
        
enemy1 = Enemy(40, 49)
enemy1.getAtk()

enemy2 = Enemy(75, 90)
enemy2.getAtk()

# #set variables
# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80

# #as long as the player is alive run
# while playerhp > 0:
#     #generate hit point and subtract it from player hp
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp = playerhp - dmg

# #set low health point
#     if playerhp <= 30:
#         playerhp = 30
        
#     print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)
# #if player hits low health print message

#     if playerhp > 30:
#         continue
        
#     print("You have low health. You have teleported to the nearest hospital")
#     #break out of while loop
#     break;
