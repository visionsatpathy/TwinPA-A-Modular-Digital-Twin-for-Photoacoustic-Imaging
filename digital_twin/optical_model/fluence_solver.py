import numpy as np


class DiffusionFluenceSolver:
    """
    Optical fluence solver using diffusion approximation.
    """

    def __init__(self, grid, incident_fluence=1.0):
        self.grid = grid
        self.incident_fluence = incident_fluence

    def compute_mu_eff(self, mu_a, mu_s, g=0.9):
        """
        Compute effective attenuation coefficient.

        Parameters
        ----------
        mu_a : float
            Absorption coefficient (1/m)
        mu_s : float
            Scattering coefficient (1/m)
        g : float
            Anisotropy factor
        """

        mu_s_prime = mu_s * (1 - g)
        mu_eff = np.sqrt(3 * mu_a * (mu_a + mu_s_prime))
        return mu_eff

    def solve(self, mu_a, mu_s):
        """
        Compute fluence map.
        """

        mu_eff = self.compute_mu_eff(mu_a, mu_s)

        fluence = np.zeros(self.grid.shape())

        for row in range(self.grid.ny):
            depth = row * self.grid.dy_m

            phi = self.incident_fluence * np.exp(-mu_eff * depth)

            fluence[row, :] = phi

        return fluence