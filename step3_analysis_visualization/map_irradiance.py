# Carte de l'irradiance solaire moyenne (GHI)
# Données : CAMS + ERA5 (dataset fusionné)

import os
import xarray as xr
import matplotlib.pyplot as plt

# Fichier d'entrée
DATA_FILE = "../data/processed/merged_temperature_irradiance.nc"

# Dossier de sortie
OUT_DIR = "../data/outputs"
OUT_FIG = os.path.join(OUT_DIR, "map_irradiance_mean.png")


def main():
    # Créer le dossier de sortie si nécessaire
    os.makedirs(OUT_DIR, exist_ok=True)

    # Charger le dataset fusionné
    ds = xr.open_dataset(DATA_FILE)

    # Sélection de la variable d'irradiance
    # (on prend la première variable CAMS trouvée)
    ghi_var = list(ds.data_vars)[0]

    # Moyenne temporelle
    ghi_mean = ds[ghi_var].mean(dim="time")

    # Création de la figure
    plt.figure(figsize=(8, 6))
    ghi_mean.plot(
        cmap="inferno",
        cbar_kwargs={"label": "Irradiance (W/m²)"}
    )

    plt.title("Irradiance solaire moyenne – Chambéry (Janvier 2023)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.tight_layout()
    plt.savefig(OUT_FIG, dpi=300)
    plt.close()

    print("Carte d’irradiance sauvegardée :", OUT_FIG)


if __name__ == "__main__":
    main()
