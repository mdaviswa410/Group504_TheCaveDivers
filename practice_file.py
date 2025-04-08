""" This is a file to practice commiting changes and pushing it to the 
    repository.
 """

import random

set1 = {"Beans", "eggs", "milk","gum"}
set2 = {"gum", "steak","eggs" }
print(f"Joined set: {set1|set2}")

random_item = random.choice(list(set1|set2))
print(f"Here is a random item from the the joined set: {random_item}")
 