# Téléchargement de l'irradiance solaire (GHI) depuis CAMS
# Source : Copernicus Atmosphere Monitoring Service (CAMS)

import os
import cdsapi
from config import BBOX, CAMS_OUT


def main():
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(os.path.dirname(CAMS_OUT), exist_ok=True)

    # Déballage de la bounding box
    north, west, south, east = BBOX

    # Client Copernicus
    c = cdsapi.Client()

    # Requête CAMS : Global Horizontal Irradiance (GHI)
    c.retrieve(
        "cams-solar-radiation-timeseries",
        {
            "sky_type": "observed_cloud",
            "time_step": "1h",
            "time_aggregation": "hourly",
            "date": "2023-01-01/2023-01-31",
            "location": {
                "north": north,
                "west": west,
                "south": south,
                "east": east,
            },
            "format": "netcdf",
        },
        CAMS_OUT,
    )

    print("Téléchargement CAMS (irradiance) terminé :", CAMS_OUT)


if __name__ == "__main__":
    main()
