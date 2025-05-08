#Function for the battle sequence algorithm focused on the attacks
import random

#Let player select weapon
def select_weapon(inventory):
    """_summary_

    Args:
        inventory (_type_): _description_

    Returns:
        _type_: _description_
    """
    #Look in inventory and present weapons
    weapon_keywords = ["Sword", "Axe", "Spear", "Flail"]
    weapons = []
    for item in inventory:
        item_label = item[0]
        for word in weapon_keywords:
            if word in item_label:
                weapons.append(item)
                break
    #Show inventory
    print("Choose a weapon:")
    for index in range(len(weapons)):
        name = weapons[index][0]
        value = weapons[index][1]
        print(f"{name} | (Attack: {value})")
    
    #Let player input a number to select their weapon since its a tuple
    while True:
        try:
            choice = int(input("Enter the number for your weapon:"))
            if choice >=1 and choice <= len(weapons):
                weapon_choice = weapons[choice - 1]
                print(f"Your weapon is: {weapon_choice[0]}.")
                return weapon_choice
            else:
                print("Invalid Number. Try again.")
        
        except ValueError:
            print("Please enter a valid number.")
        
            
                

#Battle function with parameters for the player and the enemy.
def create_battle(player_health, player_attack, player_defense,
                  enemy_health, enemy_attack, enemy_defense):
    """ Determines the strength and weakness of player and enemy damage in a
    battle.

    Args:
        player_health (int): Health of player.
        player_attack (int): Attack on the enemy, int between -5 and 5.
        player_defense (int): Players block on the enemy attack.
        enemy_health (int): Health of enemy.
        enemy_attack (int): Attack on the player, int between -5 and 5.
        enemy_defense (_int): Enemy block on the player attack.
    
    Returns:
        str: result of battle, either 'WIN', 'LOSE', or 'DRAW'
    """
    round_num = 1
#Damage taken to enemy by player and to player by enemy in between -5 and 5.
    while player_health > 0 and enemy_health > 0:
        print(f"Round {round_num}")
        damage_enemy = max(0, player_attack - enemy_defense + 
                           random.randint(-3, 3))
        enemy_health -= damage_enemy
        
        print(f"Player hit Enemy for {damage_enemy} damage. \
              Enemy health: {max(0, enemy_health)}")
        
        if enemy_health <= 0:
            break
    
        damage_player = max(0, enemy_attack - player_defense + 
                        random.randint(-3, 3))
        player_health -= damage_player
        
        if player_health <= 0:
            break
        
        print(f"Enemy hit Player for {damage_player} damage. \
              Player health: {max(0, player_health)}")
        
        round_num += 1
#Battle results based on the health of the player and enemy.
    if player_health > 0 and enemy_health <= 0:
        battle_result = 'WIN'
    elif enemy_health > 0 and player_health <= 0:
        battle_result = 'LOSE'
    else:
        battle_result = "DRAW"
    
    return battle_result.upper()