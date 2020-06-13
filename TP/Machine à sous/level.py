# Niveau 1
import random
print('"Bienvenue sur la machine à sous GravenFruitiiii')

# la liste contentant le nom des fruits
list_fruits = ['ananas', 'cerise', 'orange', 'pasteque', "pomme dorée"]

# le dictionnaire qui contient le nombre de jetons de chaque fruit en cas de victoire
tokens = {
    'ananas': 50,
    'cerise': 15,
    'orange': 5,
    'pasteque': 150,
    "pomme dorée": 10_000
}

print(list_fruits)

# affiche aléatoire un fruit de la liste
choice_fruit = random.choice(list_fruits)
print(choice_fruit)

# afficher aléatoirement 3 fruit de la liste
three_choice = random.choices(list_fruits, k=3)
print(three_choice)

# Niveau 2
prob_fruits = random.choices(list_fruits, [20, 25, 40, 10, 5], k=3)
print(prob_fruits)

if all(fruit == prob_fruits[0] for fruit in prob_fruits):
    fruit = prob_fruits[0]
    print(f'3x {str.capitalize(fruit)} - Vous gagnez {tokens[fruit]} Jetons !')
else:
    print('vous avez perdu !')
