import csv
import matplotlib.pyplot as plt

# 1. Chargement des données
donnees = []
with open('R_C3_A9partition_des_principales_installations_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2C_hors_solaire_et__C3_A9olien__2025-12-18_13-22.csv',
          newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        donnees.append(row)

# 2. Extraction des puissances
puissances = []
for i in range(len(donnees) - 1):
    row = donnees[i + 1]
    if len(row) >= 5:
        try:
            val = float(row[4].replace(',', '.'))
            puissances.append(val)
        except:
            continue

# 3. Tri des puissances par ordre décroissant
puissances.sort(reverse=True)

# 4. Préparation de l’axe horizontal
x = range(len(puissances))

# 5. Tracé de la courbe
plt.figure(figsize=(10, 6))
plt.plot(x, puissances, color='red', linewidth=2)
plt.fill_between(x, puissances, color='red', alpha=0.1)

# 6. Mise en forme du graphique
plt.title("Hiérarchie des puissances par installation (Profil de charge)")
plt.ylabel("Puissance (MW)")
plt.xlabel("Nombre d'installations classées")
plt.grid(True, linestyle='--', alpha=0.5)

# 7. Affichage du graphique
plt.show()
