import random 

#set variables
playerhp = 260
enemyatkl = 60
enemyatkh = 80

#as long as the player is alive run
while playerhp > 0:
    #generate hit point and subtract it from player hp
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

#set low health point
    if playerhp <= 30:
        playerhp = 30
        
    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)
#if player hits low health print message

    if playerhp > 30:
        continue
        
    print("You have low health. You have teleported to the nearest hospital")
    #break out of while loop
    break;
