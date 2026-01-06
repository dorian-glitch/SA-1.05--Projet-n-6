import csv
import matplotlib.pyplot as plt

# 1. Chargement (Ta méthode)
donnees_geo = []
nom_fich = 'R_C3_A9partition_des_principales_installations_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2C_hors_solaire_et__C3_A9olien__2025-12-18_13-22.csv'

with open(nom_fich, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        donnees_geo.append(row)

# 2. Extraction Longitude (X), Latitude (Y) et Puissance (Taille du point)
lons = []
lats = []
tailles = []
couleurs = []

for i in range(len(donnees_geo) - 1):
    row = donnees_geo[i+1]
    if len(row) >= 5:
        try:
            ln = float(row[1].replace(',', '.'))
            lt = float(row[2].replace(',', '.'))
            pw = float(row[4].replace(',', '.'))
            filiere = row[3]
            
            lons.append(ln)
            lats.append(lt)
            # On divise la puissance par 20 pour que les points ne soient pas trop gros
            tailles.append(pw / 20)
            
            # Couleur par type d'énergie (comme tes couleurs pour Auxerre/Sens)
            if "Nucléaire" in filiere:
                couleurs.append('red')
            elif "Hydraulique" in filiere:
                couleurs.append('blue')
            else:
                couleurs.append('green')
        except:
            continue

# 3. Tracé de la carte
plt.figure(figsize=(10, 10))

# On trace les points (s=taille du point, alpha=transparence pour voir les superpositions)
plt.scatter(lons, lats, s=tailles, c=couleurs, alpha=0.6, edgecolors='black')

# Habillage pour que ça ressemble à une carte
plt.title("Carte de la production électrique (Taille = Puissance)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, linestyle=':', alpha=0.5)

# Ajout d'une légende manuelle
plt.scatter([], [], c='red', s=50, label='Nucléaire')
plt.scatter([], [], c='blue', s=50, label='Hydraulique')
plt.scatter([], [], c='green', s=50, label='Thermique/Autre')
plt.legend(scatterpoints=1, labelspacing=1, title='Filières')

plt.show()
