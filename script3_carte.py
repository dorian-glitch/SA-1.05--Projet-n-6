import csv
import matplotlib.pyplot as plt

donnees = []
with open('R_C3_A9partition_des_principales_installations_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2C_hors_solaire_et__C3_A9olien__2025-12-18_13-22.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        donnees.append(row)

longitudes = []
latitudes = []
tailles = []

for i in range(len(donnees) - 1):
    row = donnees[i+1]
    if len(row) >= 5:
        try:
            lon = float(row[1].replace(',', '.'))
            lat = float(row[2].replace(',', '.'))
            pui = float(row[4].replace(',', '.'))
            
            longitudes.append(lon)
            latitudes.append(lat)
            tailles.append(pui / 15) 
        except:
            continue
plt.figure(figsize=(8, 8))
plt.scatter(longitudes, latitudes, s=tailles, alpha=0.6, color='blue', edgecolors='black')
plt.title("Localisation géographique des centrales en France")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, alpha=0.2)
plt.show()
