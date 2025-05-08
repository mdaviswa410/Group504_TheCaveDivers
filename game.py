import Loot_deliverable as loot
import battlesequence_interim_deliverable as battle
import interim_deliverable as challenge

def villain(name):
    if name == "gremlin":
       return{
           "name": "Gremlin", 
           "health": 30, 
           "attack": 10
           
        }
    elif name == "dragon":
        # Add some random chance to face a mini-boss or dragon
        return {
            "name": "Dragon",
            "health": 50,
            "attack": 15,
            
            }
    elif name == "boss":
        return{
           "name": "The Big Guy", 
            "health": 150, 
            "attack": 20,  
            "reward": loot.items("rare_chest")
        }
    else:
        raise ValueError("Unknown game stage")

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
            "choices": ["Fight", "Run"]
        }, 
        "Monster_Battle2":{
            "desc": "Oh no you have come across a dragon!" 
            "He is going to burn you down!", 
            "choices": ["Fight", "Run"]
        }, 
        "Monster_Battle3":{
            "desc": "The supreme boss awaits you as you approach his lair",
            "choices": ["Fight", "You must Fight"]
        }, 
        "Cave_or_Mountain":{
            "desc": "You come to a turn pass where on your left is a Mountain"
            "and a cave on your right, which do you choose?",
            "choices":["Go through cave", "Climb up the mountain"]
        }
            
    }
    
           
    game_over = False
    print(f"Welcome {name}! Your adventure is about to begin!\n")
    
    while not game_over:
        if health < 0:
            print("Game over! You have perished")
            break
        
        
        #Setting the Scene
        scene = scenes.get(location)
        print(scene['desc'])
        
        
        #Users choices
        print("\nWhat would you like to do?")
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
                print("You bravely enter the forest...and you encounter a "
                      "monster!")
                location = "Monster_Battle1"
            elif choice == "Go Back":
                print("You return to the village. The mayor is quite upset.")
                location = "small_village"
        
        elif location == "Monster_Battle1":
            gremlin = villain("gremlin")
            if choice == "Fight":
                result = battle.create_battle(health, gremlin["health"], 
                                              gremlin["attack"], 50, 15, 5)
                
                if result == 'WIN':
                   
                    print("The gremlin is defeated! Good job!")
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
                print("You run back to the village")
                location = "small_village"
                
            
        elif location == "Cave_or_Mountain":
            if choice == "Go through cave":
                print("You find a treasure chest in the cave!")
                inventory.append(loot.items("common_chest"))
                print("Your only choice is to climb up the mountain and find the" 
                      " evil dragon")
                location = "Monster_Battle2"
            elif choice == "Climb up the mountain":
                print("Uh oh! A dragon is protecting the mountain.")
                location ="Monster_Battle2"

if __name__ == "__main__":
    main()