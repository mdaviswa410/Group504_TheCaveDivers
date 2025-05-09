#How loot is found and the items that can be found 
import random
def find_chest():
    """Determines the chances of find common and rare chest
    
    Returns:
        str: common or rare
    """
    chest_type = random.choices(["common", "rare"], weights=[60, 40], k=1)[0]
    print(f"You encountered a {chest_type} chest!")
    return chest_type
    
   
def items(chest_type): 
    """Dictionary that hold items for player
    
    Args: 
        chest_type (str): the type of chest found
    
    Returns: 
        tuple: A (str, int) pair from the selected loot. item name and effect
    
    """
    
    #(changed to dict) increase/decrease player damage.
    weapons_dict = {"Wood Sword": 4, 
                    "Iron Axe": 8,
                    "Spear": 10,
                    "Spiked Flail": 12,
                    } 
    rare_weapon_dict = {"Great Sword": 15,
                        "Legendary Raider Axe": 17,
                        "Gold spear": 16,
                        "Flail of Gunter": 20,
                        }
    
    #Vlaues here should increase or decrease players health.
    potion_dict = {"Health Potion": 10,
                   "Poison Potion": 5,
                   "Nothing": 0}

    #Armor set means one item and should only affect player attributes like health.For now.
    #ie value will add to player over all health (base health + armor health)
    armor_dict = {"Filth armor": 9,
                 "Iron armor": 11} 
    rare_armor_dict = {"Armor of Life": 25,
                      "Legacy of Lebron": 100,
                      }
    
    #Combination, all common items go into common chest. same with rare. 
    # potions appear in all chests.
    common_chest = (weapons_dict|armor_dict|potion_dict)
    rare_chest = (rare_weapon_dict|rare_armor_dict|potion_dict)
    
    
    #caller calls either common or rare chest  
    selected_loot = random.choice(list(
        (rare_chest if chest_type == "rare" else common_chest).items()
        ))
    
    #Find a way to seperate the dmg value and health value in the response. Late

    print(f"You Found {selected_loot} with damage or health") 
    return selected_loot

def find_loot():
    chest_type = find_chest()
    return items(chest_type) 

if __name__ == "__main__":
    find_loot()
    #chest_type = find_chest()
    #items(chest_type)

    
    
    
    
    
