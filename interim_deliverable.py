from Loot_deliverable import find_loot
import random

challenges = {"forest_challenge" : False, "cave_challenge" : False
              ,"dark_path_challenge" : False}

def run_challenge(name_challenge, inventory):
    if challenges[name_challenge]:
        return inventory
    
    print(f"Challenge: {name_challenge.replace("_", " ").title()}")
    success = random.choice([True, False])
    
    if success:
        print("You passed the challenge, congrats")
        reward = find_loot()
        inventory.append(reward)
        print(f"You got {reward}")
    else:
        print("You failed the challenge.")
    
    challenges[name_challenge] = True
    return inventory

def check_challenges(scene_key):
    return {"Forest_entrance" : "forest_challenge"
            , "Cave_or_Mountain" : "cave_challenge"
             , "The_Dark_Path" : "dark_path_challenge"}.get(scene_key, None)

def challenge_status(name_challenge, attempted = None):
    attempted = attempted or set()
    allowed_challenges = {"forest_challenge", "cave_challenge"
              ,"dark_path_challenge"}
    return (False if (name_challenge in (attempted & allowed_challenges))
            else True)

def get_potion_dict():
    return {"Health Potion" : 10, "Nothing" : 0}
    
def heal_health(health, max_health, potions):
    if health == max_health:
        print("You have full health.")
        return health
    
    print(f"\nYour health is {health}/{max_health}")
    print("Potions to be used: ")
    for name, healing in potions.items():
        print(f"{name}: +{healing} HP")
        
    choice = input("Do you want to use a potion?: Enter name or 'no': ").strip()
    if choice in potions:
        heal = potions[choice]
        new_health = min(health + heal, max_health)
        print(f"Your current health now is {new_health}/{max_health} ")
        return new_health
    else:
        print("No potion used.")
        return health

if __name__ == "__main__":
    health = 30
    max_health = 100
    potions = get_potion_dict()
    health = heal_health(health, max_health, potions)