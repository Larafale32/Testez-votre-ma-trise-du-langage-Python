students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

def program_student():
    while True:
        name = input("Entrer le nom du étudiant : ")
        if name in students:
            print(f"\nNotes de l'étudiant {name}:")
            for subject, score in students[name].items():
                print(f"- {subject}: {score}")
                continue

            choice = input("Voulez vous afficher sa moyenne ?")
            if choice.upper() == "OUI":
                average = sum(students[name].values()) / len(students[name])
                print(f"La moyenne de {name} est de {average}.")
            elif choice.upper() == "NON":
                break
            else:
                print("Veuillez entrer 'OUI' ou 'NON'.")
        else:
            print("Cet étudiant n'existe pas.")



program_student()
