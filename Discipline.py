# Programme pour calculer la moyenne en maths

# Demande à l'utilisateur le nombre de notes
nombre_notes = int(input("Combien de notes voulez-vous entrer ? "))

# Crée une liste pour stocker les notes
notes = []

# Boucle pour récupérer toutes les notes
for i in range(nombre_notes):
    note = float(input(f"Entrez la note {i+1} : "))
    notes.append(note)

# Calcule la moyenne
moyenne = sum(notes) / nombre_notes

# Affiche le résultat
print(f"La moyenne de vos notes est : {moyenne}")
