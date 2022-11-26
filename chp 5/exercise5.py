
pets = []


pet = {
    'animal type': 'dog',
    'name': 'thursday',
    'owner': 'margaux',
    'weight': 30,
    'eats': 'chicken',
}
pets.append(pet)

pet = {
    'animal type': 'bird',
    'name': 'blue',
    'owner': 'linda',
    'weight': 5,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'yungi',
    'owner': 'hannah',
    'weight': 25,
    'eats': 'tuna',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")