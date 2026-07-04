import numpy as np


class InitialPressureSolver:
    """
    Computes initial optoacoustic pressure.
    """

    def __init__(self, gruneisen=0.12):
        self.gruneisen = gruneisen

    def compute(self, mu_a_map, fluence_map):
        """
        p0 = Gamma * mu_a * Phi
        """

        if mu_a_map.shape != fluence_map.shape:
            raise ValueError("Shape mismatch between maps")

        p0 = (
            self.gruneisen *
            mu_a_map *
            fluence_map
        )

        return p0