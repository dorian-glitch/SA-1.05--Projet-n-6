# Importe les modules nécessaires pour tracer la courbe
import csv
import matplotlib.pyplot as plt

#Chargement des données
donnees = []
with open('R_C3_A9partition_des_principales_installations_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2C_hors_solaire_et__C3_A9olien__2025-12-18_13-22.csv',
          newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        donnees.append(row)

#Extraction des puissances
puissances = []
for i in range(len(donnees) - 1):
    row = donnees[i + 1]
    if len(row) >= 5:
        try:
            val = float(row[4].replace(',', '.'))
            puissances.append(val)
        except:
            continue

#Tri des puissances par ordre décroissant
puissances.sort(reverse=True)

# Préparation de l’axe des abscisses
x = range(len(puissances))

#Tracé de la courbe
plt.figure(figsize=(10, 6))
plt.plot(x, puissances, color='red', linewidth=2)
plt.fill_between(x, puissances, color='red', alpha=0.1)

#Mise en forme du graphique
plt.title("Hiérarchie des puissances par installation (Profil de charge)")
plt.ylabel("Puissance (MW)")
plt.xlabel("Nombre d'installations classées")
plt.grid(True, linestyle='--', alpha=0.5)

#Affichage du graphique
plt.show()
