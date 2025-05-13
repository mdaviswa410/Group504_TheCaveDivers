import Loot_deliverable as potions
# The variable CHALLENGES is a global variable for easy use anywhere.
CHALLENGES = {"Chal1" : 1, "Chal2" : 1, "Chal3" : 1, "Chal4" : 2, "Chal5" : 2, 
              "Chal6" : 2, "Chal7" : 3, "Chal8" : 3, "Chal9" : 3, "Chal10" : 4, 
              "Chal11" : 4, "Chal12" : 4, "Chal13" : 5, "Chal14" : 5, "Chal15" : 5}

def challenges(hero_level):
    """This will append challenges the hero can take
    
    Args:
    hero_level (int): The level of the hero
    
    Returns:
    available: A list of challenges when conditions are met the hero can do.
    
    Side effects:
    The variable available is created as a list that has task appended.
    
    """
    
    available = []
    for task, level in CHALLENGES.items():
        if level == hero_level:
            available.append(task)
        
    return available

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