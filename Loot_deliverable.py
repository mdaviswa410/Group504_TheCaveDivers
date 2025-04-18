# April 18 single function algo
#All comments are notes to myself, not specifically what 

def items(weapons, potions, armor):
    #(changed to dict) increase/decrease player damage (maybe add a rare set. some chest could have only rare and other a combined chance of both)
    weapons_dict = {"Wood Sword": 4, 
                    "Iron Axe": 8,
                    "Spear": 10,
                    "Spiked Flail": 12} 
    rare_weapon_dict = {"Great Sword": 15,
                        "Legendary Raider Axe": 17,
                        "Gold spear": 16,
                        "Flail of Gunter": 20
                        
                        }
    
    #Combined weapon dict to append to treasure. (maybe i append/return it to chest algo)
    combined_weapon_dict = {weapons_dict|rare_weapon_dict} 
   
   #vlaues here should increase or decrease players health
    potion_dict = {"Health Potion": 10,
                   "Poision Potion": 5} 
    #for lack of time armor set means one item, and ahould only affect player attributes like health etc for now
    #ie value will add to player over all health (base health + armor health)
    armor_set = {"iron armor": 10,
                 ""} 
    rare_armor_set = {}
    
    # while loop if chest == true select from dictionary and return selected item 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    player_inventory = {} #add items found as key and quantity of items found as values....??