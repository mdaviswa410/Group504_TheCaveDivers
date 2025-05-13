#How loot is found and the items that can be found 
import random
import time
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
                        "Lightning Spear": 24,
                        "Excessum Fatum": 26,
                        "Orion's Fire Axe": 30,}
    
    #Vlaues here should increase or decrease players health.
    potion_dict = {"Health Potion": 10,
                   "Poison Potion": 5,
                   "Nothing": 0}

    #Armor set means one item and should only affect player attributes like health.For now.
    #ie value will add to player over all health (base health + armor health)
    armor_dict = {"Filth Armor": 9,
                  "Broken Armor": 10,
                 "Iron Armor": 17,
                 "Poor Armor":14} 
    rare_armor_dict = {"Life Armor": 20,
                        "Symphony of the Unheard Armor":24,
                      "Legacy of Lebron Armor": 100,
                      "Death of Field Armor": 22}
    
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

def sleep_count():
    print("........Exploring.......")
    time.sleep(2)  #sleep for 2 sec and act ass exploring
    

if __name__ == "__main__":
    find_loot()
    sleep_count()
    #chest_type = find_chest()
    #items(chest_type)


    
       
    
    
    
    
