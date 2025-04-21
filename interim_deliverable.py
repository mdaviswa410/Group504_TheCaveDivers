CHALLENGES = {"Chal1" : 1, "Chal2" : 1, "Chal3" : 1, "Chal3" : 2, "Chal4" : 2, 
              "Chal5" : 2, "Chal6" : 3, "Chal7" : 3, "Chal8" : 3, "Chal9" : 4, 
              "Chal10" : 4, "Chal11" : 4, "Chal12" : 5, "Chal13" : 5, "Chal14" : 5}


def challenges():
    available = []
    for task, level in CHALLENGES:
        if level == hero_level:
            available.append(task)
        
    return available