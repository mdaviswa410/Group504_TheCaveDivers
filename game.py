import Loot_deliverable as loot
import battlesequence_interim_deliverable as battle
import interim_deliverable as challenge

def villain(name):
    if name == "gremlin":
       return{
           "name": "Gremlin", 
           "health": 30, 
           "attack": 5
           
        }
    elif name == "dragon":
        # Add some random chance to face a mini-boss or dragon
        return {
            "name": "Dragon",
            "health": 50,
            "attack": 10,
            
            }
    elif name == "boss":
        return{
           "name": "The Big Guy", 
            "health": 150, 
            "attack": 15,  
            "reward": loot.find_loot()
        }
    else:
        raise ValueError("Unknown game stage")

def use_item(player_health, player_attack, player_defense, inventory):
    chest_type = loot.find_chest()
    item_name, effect_value = loot.items(chest_type)
    
    
    if any(keyword in item_name for keyword in ["Sword", "Axe", "Spear", "Flail"]):
        player_attack += effect_value
        print(f"You equipped {item_name}")
        
    elif "Potion" in item_name:
        if "Poison" in item_name:
            player_attack -= effect_value
            print(f"Oh no! {item_name}")
        else:
            player_health = challenge.heal_health(player_health, max_health=100, potions=item_name)
            print(f"You used {item_name}")
    elif "armor" in item_name or "Armor" in item_name:
        player_defense += effect_value
        print(f"You equipped {item_name}!")
    else:
        print(f"{item_name} had no effect.")
        
    return player_health, player_attack, player_defense
    

   
"""
    
    This is a simple text-based rpg game where the user plays the role of the 
    hero. As the adventure goes on the harder it gets.
    
    How it works:
    The user will type in the number of the choice they want to pick and their 
    actions will have specific consequences as the game progresses. 
    
    """
def main():
    """
    Runs the main framework for our rpg game.
    
    Prompts the player for responses with choices
    
    Side Effects:
        Uses the print statement to output things to the console
        Uses input to change the choice made. 
    """
    

    #Initilizing the game
    
    name = input("Enter your name hero: ")
    inventory = []
    location = "small_village"
    health = 100
    attack = 10
    defense = 5
    previous_choice = []
    
    
    scenes = {
        "small_village":{
            "desc": "You wake up in a small village, everything is peaceful."
                    "The birds are chirping and there is a slight breeze." 
                    " All of a sudden you here a knock at the door."
                    "\n Please choose a number:", 
            "choices": ["Open Door", "Stay in bed"]
        },
        "Open_Door":{
            "desc": "You open the door and the town mayor approaches you. "
                "He says he needs you help fighting off the monsters in time "
                "for the village party.",
            "choices": ["Accept", "Decline"]
        },
        "Forest_entrance":{
            "desc": "The forest looks dark and dangerous.",
            "choices": ["Enter Forest", "Go Back"]
            
        },
        "Monster_Battle1":{
            "desc": "Infront of you stands an evil gremlin!",
            "choices": ["Fight", "Run", "Use Item"]
        }, 
        "Monster_Battle2":{
            "desc": "Oh no you have come across a dragon!" 
            "He is going to burn you down!", 
            "choices": ["Fight", "Run", "Use Item"]
        }, 
        "Monster_Battle3":{
            "desc": "The supreme boss stomps infront of the chest and roars at you",
            "choices": ["Fight", "Use Item"]
        }, 
        "Cave_or_Mountain":{
            "desc": "You come to a turn pass where on your left is a Mountain"
            " and a cave on your right, which do you choose?",
            "choices":["Go through cave", "Climb up the mountain"]
        }, 
        "The_Dark_Path":{
            "desc": "Ahead is a dark path, but you feel the urge to go down it.", 
            "choices":["Go down the path", "Leave"]
        }, 
        
        "Safe_return":{
            "desc": (f"Good job {name}! You have defeated the boss and returned"
            " to your village. "), 
            "choices": ["End Game"]
            
        }
            
    }
    
           
    game_over = False
    print(f"Welcome {name}! Your adventure is about to begin!\n")
    
    while not game_over:
        if health <= 0:
            print("Game Over!")
            break
        
        
        #Setting the Scene
        scene = scenes.get(location)
        print(scene['desc'])
        
        
        #Users choices
        print("\nWhat would you like to do?")
        print(f"{name}'s health is: {health}%.")
        for choice in range(len(scene['choices'])):
            print(f"{choice + 1}. {scene['choices'][choice]}")
            
            
        #Get Choice
        try: 
            choice_index = int(input("Choose an option (Based on the number "
                                     "of the option): "))
            if choice_index < 1 or choice_index > len(scene['choices']):
                print("Invalid choice, please pick again!")
                continue
        except ValueError:
            print("Please enter a number: ")
            continue
        
        choice = scene['choices'][choice_index - 1]
        previous_choice.append(choice)
        print(f"\nYou have chosen: {choice}\n") 
        
        #Choices playing out
        if location == "small_village":
            if choice == "Open Door":
                location = "Open_Door"
            elif choice == "Stay in bed":
                print( "You get five more minutes of sleep but the knocking"               
                "keeps going. You go to the doorway.")
                location = "Open_Door"
    
        elif location == "Open_Door":
            if choice == "Accept":
                location = "Forest_entrance"
               
            elif choice == "Decline":
                print("You refused to help. The mosters destroy your village "
                        "Game over!")
                game_over = True
                
        elif location == "Forest_entrance" :
            if choice == "Enter Forest":
                loot.sleep_count() #Exploring the new area
                print("You find a treasure chest in the forest!")
                gained = loot.find_loot()  #Added to give plyer start item
                inventory.append(gained)
                print(f"You got: {gained[0]}")
                loot.sleep_count()
                print("You bravely explored the forest...and you encounter a "
                      "monster!")
                location = "Monster_Battle1"
            elif choice == "Go Back":
                print("You return to the village. The mayor is quite upset.")
                location = "small_village"
        
        elif location == "Monster_Battle1":
            gremlin = villain("gremlin")
            
            if choice == "Fight":
                weapon = battle.select_weapon(inventory)
                if weapon:
                    weapon_name, weapon_value = weapon
                    attack += weapon_value
                result, health, _ = battle.create_battle(health, attack, defense,
                                        gremlin["health"], gremlin["attack"], 5)
                
                if result == 'WIN':
                    print("The gremlin is defeated! Good job!\n")
                    location = "Cave_or_Mountain"
                
                elif result == 'LOSE':
                    health -= 30
                    print(f"Oh no! Your health is now {health}")
                    if health <= 0:
                        print("You died, game over.")
                        game_over = True
                    else: 
                        location = "Forest_entrance"
                
            elif choice == "Run":
                print("You run back to the village...\n")
                location = "small_village"
                
            elif choice == "Use Item":
                health, attack, defense = use_item(health, attack, defense, inventory)
                print("You feel stronger, time to face the gremlin!")
                
            
                
                
            
        elif location == "Cave_or_Mountain":
            if choice == "Go through cave":
                print(f"You entered the cave")
                loot.sleep_count()
                print("You find a treasure chest in the cave!")
                gained = loot.find_loot()
                inventory.append(gained)
                print(f"You got: {gained[0]}")
                loot.sleep_count()
                print("Your only choice is to climb up the mountain and find the" 
                      " evil dragon")
                location = "Monster_Battle2"
            elif choice == "Climb up the mountain":
                loot.sleep_count()
                print("Uh oh! A dragon is protecting the mountain.")
                location ="Monster_Battle2"
                
        elif location == "Monster_Battle2":
            dragon = villain("dragon")
            
            if choice == "Fight":
                weapon = battle.select_weapon(inventory)
                if weapon:
                    weapon_name, weapon_value = weapon
                    attack += weapon_value
                result, health, _ = battle.create_battle(health, attack, defense,
                                        dragon["health"], dragon["attack"], 10)
                 
                
                if result == 'WIN':
                    print("The dragon is defeated! Good job!")
                    location = "The_Dark_Path"
                
                else:
                    health -= 30
                    print(f"Oh no! Your health is now {health}")
                    if health <= 0:
                        print("You died, game over.")
                        game_over = True
                        
            elif choice == "Run":
                print("You run back to the village")
                location = "small_village"
                
            elif choice == "Use Item":
                health, attack, defense = use_item(health, attack, defense, inventory)
            
        elif location == "The_Dark_Path":
            
            if choice == "Go down the path":
                loot.sleep_count()
                print("You see a huge golden chest infront of you. "
                          "Not only would you protect the village but also save "
                          "save the economy!\n")
                location = "Monster_Battle3"
            elif choice == "Leave":
                location = "small_village"
                    
        elif location == "Monster_Battle3":
            
            boss = villain("boss")
            
            if choice == "Fight":
                weapon = battle.select_weapon(inventory)
                if weapon:
                    weapon_name, weapon_value = weapon
                    attack += weapon_value
                result, health, _ =  battle.create_battle(health, attack, defense, 
                                    boss["health"], boss["attack"], 15)
                if result == 'WIN':
                   
                    print("The boss is defeated! Good job!")
                    location = "Safe_return"
                    print(f"You recieved: {boss['reward'][0]}")
                
                elif result == 'LOSE':
                    health -= 60
                    print(f"Oh no! Your health is now {health}")
                    if health <= 0:
                        print("[You died, game over.]")
                        game_over = True
                    else: 
                        location = "Safe_return"
                        
            elif choice == "Run":
                print("You run back to the village")
                location = "small_village"
                
            elif choice == "Use Item":
                health, attack, defense = use_item(health, attack, defense, inventory)            
        elif location == "Safe_return":
            if choice == "End Game":
                print(scenes["Safe_return"]["desc"])
                game_over = True



if __name__ == "__main__":
    main()