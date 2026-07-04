from dataclasses import dataclass


@dataclass
class TissueMaterial:
    """
    Tissue material definition for optoacoustic simulation.
    Units:
        mu_a               -> 1/m
        mu_s              -> 1/m
        speed_of_sound    -> m/s
        density           -> kg/m^3
        attenuation_db    -> dB/(MHz*cm)
    """
    name: str
    mu_a: float
    mu_s: float
    gruneisen: float
    speed_of_sound: float
    density: float
    attenuation_db: float


class MaterialLibrary:
    WATER = TissueMaterial(
        name="Water",
        mu_a=0.01,
        mu_s=0.0,
        gruneisen=0.11,
        speed_of_sound=1480,
        density=1000,
        attenuation_db=0.002
    )

    BLOOD = TissueMaterial(
        name="Blood",
        mu_a=120.0,
        mu_s=8000.0,
        gruneisen=0.20,
        speed_of_sound=1570,
        density=1060,
        attenuation_db=0.2
    )

    FAT = TissueMaterial(
        name="Fat",
        mu_a=8.0,
        mu_s=12000.0,
        gruneisen=0.70,
        speed_of_sound=1450,
        density=920,
        attenuation_db=0.6
    )

    MUSCLE = TissueMaterial(
        name="Muscle",
        mu_a=15.0,
        mu_s=15000.0,
        gruneisen=0.12,
        speed_of_sound=1580,
        density=1050,
        attenuation_db=1.0
    )