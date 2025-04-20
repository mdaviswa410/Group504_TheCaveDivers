# April 18 single function algo
#All comments are notes to myself 
import random
def items(chest_type): #weapons, potions, armor
    """Chest will be a string that calls rare or common
    
    """
    #player_inventory = {} #add items found as key and quantity of items found 
    # as values....?? Add later or in a different fucntion
    
    #(changed to dict) increase/decrease player damage.
    weapons_dict = {"Wood Sword": 4, 
                    "Iron Axe": 8,
                    "Spear": 10,
                    "Spiked Flail": 12,
                    "Nothing": 0} 
    rare_weapon_dict = {"Great Sword": 15,
                        "Legendary Raider Axe": 17,
                        "Gold spear": 16,
                        "Flail of Gunter": 20,
                        "Nothing": 0}
    
    #Vlaues here should increase or decrease players health.
    potion_dict = {"Health Potion": 10,
                   "Poison Potion": 5,
                   "Nothing": 0}

    #Armor set means one item and should only affect player attributes like health.For now.
    #ie value will add to player over all health (base health + armor health)
    armor_dict = {"Flith armor": 9,
                 "Iron armor": 11} 
    rare_armor_dict = {"Armor of ": 25,
                      "Legacy of Lebron": 100,
                      "Nothing": 0}
    
    #Combination, all common items go into common chest. same with rare. 
    # potions appear in all chests.
    common_chest = (weapons_dict|armor_dict|potion_dict)
    rare_chest = (rare_weapon_dict|rare_armor_dict|potion_dict)
    

    #if common_chest 
    #selected_loot = random.choice(list(common_chest.items()))
    
    #conditional expression in the slot ()
    
    #caller calls either common or rare chest  
    selected_loot = random.choice(list(
        (rare_chest if chest_type == "rare" else common_chest).items()
        ))
    
    #Find a way to seperate the dmg value and health value in the response. Late

    print(f"You Found {selected_loot} with damage or health") 
    return selected_loot
    
#if __name__ == "__main__":
items("rare")
    
    
    
    
    
