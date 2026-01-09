# Permet de lire un fichier CSV et de tracer des graphiques
import csv
import matplotlib.pyplot as plt

# Ouvre le fichier, lit son contenu, définit le délimiteur entre les colonnes
# et stocke toutes les lignes dans une liste
donnees = []
with open("fichier1.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        donnees.append(row)

# Création des listes
dates = []
valeurs = []
filieres = []

# Saute l’en-tête du fichier
for i in range(len(donnees) - 1):
    row = donnees[i + 1]

    # Range chaque information dans la bonne variable
    date = row[0]
    filiere = row[1]

    # Crée les différentes listes pour toutes les données
    # et sautes les lignes vide
    if row[2] != "":
        valeur = float(row[2].replace(",", "."))
        dates.append(date)
        valeurs.append(valeur)
        filieres.append(filiere)

# Crée les différentes courbes pour chaque filière
for filiere in set(filieres):
    x = []
    y = []
    for i in range(len(filieres)):
        if filieres[i] == filiere:
            x.append(dates[i])
            y.append(valeurs[i])
    plt.plot(x, y, label=filiere)

# Réalisation du graphique
plt.title("Production d'électricité par filière")
plt.xlabel("Date")
plt.ylabel("Valeur (TWh)")
plt.legend()
plt.show()

