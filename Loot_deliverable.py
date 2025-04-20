# April 18 single function algo
#All comments are notes to myself 
import random
def items(): #weapons, potions, armor
    player_inventory = {} #add items found as key and quantity of items found as values....??
    
    #(changed to dict) increase/decrease player damage (maybe add a rare set. some chest could have only rare and other a combined chance of both)
    weapons_dict = {"Wood Sword": 4, 
                    "Iron Axe": 8,
                    "Spear": 10,
                    "Spiked Flail": 12} 
    rare_weapon_dict = {"Great Sword": 15,
                        "Legendary Raider Axe": 17,
                        "Gold spear": 16,
                        "Flail of Gunter": 20}
    
    #Combined weapon dict to append to treasure. (maybe i append/return it to chest algo)
       #vlaues here should increase or decrease players health
    potion_dict = {"Health Potion": 10,
                   "Poision Potion": 5}

    #for lack of time armor set means one item, and ahould only affect player attributes like health etc for now
    #ie value will add to player over all health (base health + armor health)
    armor_set = {"Flith armor": 9,
                 "Iron armor": 11} 
    rare_armor_set = {"Armor of ": 25,
                      "Legacy of Lebron": 100}
    
    #Combination, all common items go into common chest. same with rare. potions appear in all chests.
    common_chest = weapons_dict|armor_set|potion_dict
    rare_chest = rare_weapon_dict|rare_armor_set|potion_dict
    
    # while loop if chest == true select from dictionary and return selected item 
    #testing before loop
    selected_loot = random.choice(list(common_chest.items()))
    print(f"You Found {selected_loot} with damage or health") #Find a way to seperate the dmg value and health value in the response
    #player_inventory.appe
    #return player_inventory
    
if __name__ == "__main__":
    items()
    
    
    
    
    
    
    
    
