import csv
import matplotlib.pyplot as plt

# 1. Chargement des données
donnees = []
with open('R_C3_A9partition_des_principales_installations_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2C_hors_solaire_et__C3_A9olien__2025-12-18_13-22.csv',
          newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        donnees.append(row)

# 2. Calcul de la puissance totale par filière
filiere_totaux = {}

for i in range(len(donnees) - 1):
    row = donnees[i + 1]
    if len(row) >= 5:
        nom_filiere = row[3]
        try:
            pui = float(row[4].replace(',', '.'))
            if nom_filiere in filiere_totaux:
                filiere_totaux[nom_filiere] += pui
            else:
                filiere_totaux[nom_filiere] = pui
        except:
            continue

# 3. Préparation des données pour le graphique
noms = list(filiere_totaux.keys())
valeurs = list(filiere_totaux.values())

# 4. Tracé de l’histogramme
plt.figure(figsize=(10, 6))
plt.bar(noms, valeurs, color='orange', edgecolor='black')

# 5. Mise en forme du graphique
plt.title("Puissance totale installée par filière (MW)")
plt.ylabel("Puissance cumulée (MW)")

# 6. Affichage du graphique
plt.show()
