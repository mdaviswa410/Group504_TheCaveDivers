from battlesequence_interim_deliverable import create_battle

battle_result = create_battle(
    player_health = 80, player_attack = 12, player_defense = 4,
    enemy_health = 80, enemy_attack = 10, enemy_defense = 2
)

print (battle_result)