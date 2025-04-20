import random

CHALLENGES = {"Chal1" : 1, "Chal2" : 1, "Chal3" : 1, "Chal3" : 2, "Chal4" : 2, 
              "Chal5" : 2, "Chal6" : 3, "Chal7" : 3, "Chal8" : 3, "Chal9" : 4, 
              "Chal10" : 4, "Chal11" : 4, "Chal12" : 5, "Chal13" : 5, "Chal14" : 5}


def challenges():
    available = []
    for task, level in CHALLENGES:
        if level == hero_level:
            available.append(task)
        
    return available
    
    
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