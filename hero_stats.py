#Create a dictionary for your character's stats
hero_stats = {
    "health": 100,
    "mana": 50,
    "stamina": 75
}
#A monster attacked subtract 20 from health
hero_stats["health"] -=20
#Add a new key called "exp"
hero_stats["exp"] = 0
print(hero_stats)