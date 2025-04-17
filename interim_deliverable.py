import random

def create_battle(player_health, player_attack, player_defense,
                  enemy_health, enemy_attack, enemy_defense):
    round_num = 1
    while player_health > 0 and enemy_health > 0:
        return f"Round {round_num}"
        damage_enemy = max(0, player_attack - enemy_defense + 
                           random.randint(-5, 5))
        enemy_health -= damage_enemy
    
        if enemy_health <= 0:
            break
    
        damage_player = max(0, enemy_attack - player_defense + 
                        random.randint(-5, 5))
        player_health -= damage_player
        round_num += 1
    
    game_result = None