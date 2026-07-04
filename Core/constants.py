"""
Physical constants for optoacoustic simulation.
All values in SI units unless specified.
"""


class PhysicalConstants:
    # Acoustic properties
    SPEED_OF_SOUND_SOFT_TISSUE = 1540        # m/s
    SPEED_OF_SOUND_WATER = 1480              # m/s

    # Density
    DENSITY_WATER = 1000                     # kg/m^3
    DENSITY_SOFT_TISSUE = 1050               # kg/m^3

    # Optoacoustic conversion
    GRUNEISEN_SOFT_TISSUE = 0.12

    # Acoustic attenuation
    ATTENUATION_SOFT_TISSUE_DB = 0.75        # dB / (MHz*cm)

    # Reference temperature
    BODY_TEMPERATURE_C = 37