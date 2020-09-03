import random 


playerhp = 260
enemyatkl = 60
enemyatkh = 80

#as long as the player has health they can be attacked
while playerhp > 0:
   dmg = random.randrange(enemyatkl, enemyatkh)