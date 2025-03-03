words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
voyelles = ['a', 'e', 'i', 'o', 'u', 'y']


for mot in words:
    total_voyelles = sum(mot.count(v) for v in voyelles)
    tuple_mots = (mot, total_voyelles)
    print(tuple_mots)

