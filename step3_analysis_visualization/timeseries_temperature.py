# Série temporelle de la température (ERA5) au centre de la zone
# Données : dataset fusionné (CAMS + ERA5)

import os
import xarray as xr
import matplotlib.pyplot as plt

DATA_FILE = "../data/processed/merged_temperature_irradiance.nc"

OUT_DIR = "../data/outputs"
OUT_FIG = os.path.join(OUT_DIR, "timeseries_temperature.png")


def find_temperature_variable(ds):
    # ERA5 2m temperature is often stored as "t2m" or "2m_temperature"
    for v in ["t2m", "2m_temperature"]:
        if v in ds.data_vars:
            return v
    # fallback: choose a variable name that contains "temp"
    for v in ds.data_vars:
        if "temp" in v.lower():
            return v
    # last resort: return the last variable
    return list(ds.data_vars)[-1]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    ds = xr.open_dataset(DATA_FILE)

    t_var = find_temperature_variable(ds)
    da = ds[t_var]

    # Convert Kelvin -> Celsius if values look like Kelvin
    # (ERA5 temperature is in Kelvin)
    if float(da.mean()) > 100:
        da_c = da - 273.15
        y_label = "Température (°C)"
    else:
        da_c = da
        y_label = "Température (unité dataset)"

    # pick central point of the domain
    lat0 = float(ds["lat"].mean())
    lon0 = float(ds["lon"].mean())

    point = da_c.sel(lat=lat0, lon=lon0, method="nearest")

    plt.figure(figsize=(10, 4))
    plt.plot(point["time"].values, point.values)
    plt.title(f"Série temporelle de la température au point (~{lat0:.3f}, {lon0:.3f})")
    plt.xlabel("Temps")
    plt.ylabel(y_label)
    plt.tight_layout()

    plt.savefig(OUT_FIG, dpi=300)
    plt.close()

    print("Série temporelle sauvegardée :", OUT_FIG)


if __name__ == "__main__":
    main()
