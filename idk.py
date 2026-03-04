import random
import json

# Charger le dictionnaire depuis le fichier JSON
with open('wordsDictionary.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Sélectionner une langue aléatoire
langue = random.choice(list(words.keys()))

# Sélectionner un mot aléatoire dans cette langue
mot_data = random.choice(words[langue])

# Afficher le résultat
print(f"\n🌍 Langue : {langue.upper()}")
print(f"📝 Mot : {mot_data['mot']}")
print(f"💬 Traduction : {mot_data['traduction']}")
print(f"🔊 Prononciation : {mot_data['prononciation']}\n")
