import random

medals = ["First Medal", "Second Medal", "Third Medal"]
medals_obtained = []

def challenge_status(name_challenge, attempted = None):
    attempted = attempted or set()
    allowed_challenges = {"forest_challenge", "cave_challenge"
              ,"dark_path_challenge"}
    return (False if (name_challenge in (attempted & allowed_challenges))
            else True)

def run_challenges(scene_key, medals, inventory, attempted):
    names = {"Forest_entrance" : "forest_challenge", 
             "Cave_or_Mountain" : "cave_challenge",
             "The_Dark_Path" : "dark_path_challenge"}
    
    type_challenge = {"forest_challenge" : "coin", "cave_challenge" : "number",
                      "dark_path_challenge" : "dice"}
    
    names_challenges = names.get(scene_key)
    if not names_challenges:
        print("No challenge")
        return inventory
    
    if not challenge_status(names_challenges, attempted):
        print("You already attempted this")
        return inventory
    
    print(f"\n {names_challenges.replace("_", " ").title()}")
    attempted.add(names_challenges)
    kind = type_challenge[names_challenges]
    success = False
    
    if kind == "coin":
        guess = input("Guess heads or tails: ").strip().lower()
        result = random.choice(["heads", "tails"])
        print(f"The coin lands on {result}")
        success = (guess == result)
    
    elif kind == "number":
        try:
            guess = int(input("Guess a number between 1 to 4: "))
            actual_num = random.randint(1, 4)
            print(f"The number is {actual_num}")
            success = (guess == actual_num)
        except ValueError:
            print("Invalid number")
    
    elif kind == "dice":
        try:
            guess = int(input("Guess a dice roll between 1 to 6: "))
            actual_roll = random.randint(1, 6)
            print(f"Dice roll is {actual_roll}")
            success = (guess == actual_roll)
        except ValueError:
            print("Invalid number")

    if success:
        if medals:
            reward = medals.pop(0)
            inventory.append(reward)
            print(f"You won {reward}")
        else:
            print("You have completed challenge, but there is no medals left")
    else:
        print("You lost this challenge")
    return inventory

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
    max_health = 50
    potions = get_potion_dict()
    health = heal_health(health, max_health, potions)