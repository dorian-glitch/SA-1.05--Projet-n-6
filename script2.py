import csv
import numpy as np
from matplotlib import pyplot as plt

# 1. Chargement des données
donnees = []
with open('_C3_89volution_du_parc_install_C3_A9_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2025-12-18_13-39.csv',
          newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)
    for row in reader:
        if len(row) >= 3 and row[2] != '':
            donnees.append(row)

# 2. Création des listes de stockage
dates = []
solaire_pop = []
thermique_pop = []

# 3. Séparation des données par filière
for row in donnees:
    annee = int(row[0])
    filiere = row[1]
    valeur = float(row[2].replace(',', '.'))

    if filiere == "Solaire":
        if annee not in dates:
            dates.append(annee)
        solaire_pop.append(valeur)

    if filiere == "Thermique fossile":
        thermique_pop.append(valeur)

# 4. Tracé des points (nuage de points)
plt.scatter(dates, solaire_pop, color='orange', label='Solaire')
plt.scatter(dates, thermique_pop, color='grey', label='Thermique fossile')

# 5. Calcul des régressions linéaires
dates_projection = [2007, 2030]

coef_sol = np.polyfit(dates, solaire_pop, 1)
poly_sol = np.poly1d(coef_sol)
plt.plot(dates_projection, poly_sol(dates_projection),
         color='orange', linestyle='dashed')

coef_ther = np.polyfit(dates, thermique_pop, 1)
poly_ther = np.poly1d(coef_ther)
plt.plot(dates_projection, poly_ther(dates_projection),
         color='grey', linestyle='dashed')

# 6. Mise en forme du graphique
plt.title("Évolution de la puissance installée en France (GW)")
plt.ylabel('Puissance (GW)')
plt.xlabel('Années')
plt.legend()

# 7. Affichage du graphique
plt.show()
