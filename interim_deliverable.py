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

def pass_or_fail(challenge):
    pass