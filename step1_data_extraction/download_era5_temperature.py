# Téléchargement de la température de l'air à 2 m (ERA5)
# Source : Copernicus Climate Data Store (ERA5)

import os
import cdsapi
from config import BBOX, START_DATE, END_DATE, ERA5_OUT


def main():
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(os.path.dirname(ERA5_OUT), exist_ok=True)

    # Déballage de la bounding box
    north, west, south, east = BBOX

    # Client Copernicus
    c = cdsapi.Client()

    # Requête ERA5 : température à 2 m
    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": "2m_temperature",
            "year": "2023",
            "month": "01",
            "day": [f"{d:02d}" for d in range(1, 32)],
            "time": [f"{h:02d}:00" for h in range(24)],
            "area": [
                north,
                west,
                south,
                east,
            ],
            "format": "netcdf",
        },
        ERA5_OUT,
    )

    print("Téléchargement ERA5 terminé :", ERA5_OUT)


if __name__ == "__main__":
    main()
