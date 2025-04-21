#Function for the battle sequence algorithm focused on the attacks
import random
#Battle function with parameters for the player and the enemy.
def create_battle(player_health, player_attack, player_defense,
                  enemy_health, enemy_attack, enemy_defense):
    round_num = 1
#Damage taken to enemy by player and to player by enemy in between -5 and 5.
    while player_health > 0 and enemy_health > 0:
        print(f"Round {round_num}")
        damage_enemy = max(0, player_attack - enemy_defense + 
                           random.randint(-5, 5))
        enemy_health -= damage_enemy
    
        if enemy_health <= 0:
            break
    
        damage_player = max(0, enemy_attack - player_defense + 
                        random.randint(-5, 5))
        player_health -= damage_player
        round_num += 1
#Battle results based on the health of the player and enemy.
    if player_health > 0 and enemy_health <= 0:
        battle_result = 'WIN'
    elif enemy_health > 0 and player_health <= 0:
        battle_result = 'LOSE'
    else:
        battle_result = "DRAW"
    
    return f"Battle Result: {battle_result.upper()}"