# Fusion et nettoyage des données ERA5 (température) et CAMS (irradiance)
# Résultat : un seul dataset NetCDF géoréférencé

import os
import xarray as xr

# Fichiers d'entrée
CAMS_IN = "../data/raw/cams_radiation.nc"
ERA5_IN = "../data/raw/era5_temperature.nc"

# Fichier de sortie
OUT_FILE = "../data/processed/merged_temperature_irradiance.nc"


def standardize_coordinates(ds):
    """
    Harmonise les noms des coordonnées latitude / longitude
    """
    rename_dict = {}

    if "latitude" in ds.coords:
        rename_dict["latitude"] = "lat"
    if "longitude" in ds.coords:
        rename_dict["longitude"] = "lon"

    if rename_dict:
        ds = ds.rename(rename_dict)

    return ds


def main():
    # Créer le dossier de sortie si nécessaire
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

    # Ouvrir les datasets
    cams = xr.open_dataset(CAMS_IN)
    era5 = xr.open_dataset(ERA5_IN)

    # Harmoniser les coordonnées
    cams = standardize_coordinates(cams)
    era5 = standardize_coordinates(era5)

    # Aligner les données sur le temps commun
    cams, era5 = xr.align(cams, era5, join="inner")

    # Fusionner les datasets
    merged = xr.merge([cams, era5])

    # Ajouter des métadonnées
    merged.attrs["description"] = (
        "Dataset fusionné : irradiance solaire (CAMS) "
        "et température de l'air à 2 m (ERA5)"
    )
    merged.attrs["source"] = "Copernicus Climate Data Store (ERA5) & CAMS"
    merged.attrs["region"] = "Chambéry, France"
    merged.attrs["period"] = "Janvier 2023"

    # Sauvegarde
    merged.to_netcdf(OUT_FILE)

    print("Fusion terminée. Fichier créé :", OUT_FILE)


if __name__ == "__main__":
    main()
