import numpy as np


class PhantomBuilder:
    """
    Creates synthetic phantoms on a simulation grid.
    """

    def __init__(self, grid):
        self.grid = grid
        self.mask = np.zeros(grid.shape(), dtype=float)

    def add_circle(self, center_x_mm, center_y_mm, radius_mm, value=1.0):
        """
        Add circular feature to phantom.

        Parameters
        ----------
        center_x_mm : float
        center_y_mm : float
        radius_mm   : float
        value       : float
        """

        center_x_m = center_x_mm * 1e-3
        center_y_m = center_y_mm * 1e-3
        radius_m = radius_mm * 1e-3

        distance = np.sqrt(
            (self.grid.X - center_x_m) ** 2 +
            (self.grid.Y - center_y_m) ** 2
        )

        circle_mask = distance <= radius_m
        self.mask[circle_mask] = value

    def get_mask(self):
        return self.mask