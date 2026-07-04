
import numpy as np


class SimulationGrid:
    """
    Defines spatial discretization for optoacoustic simulations.

    Units:
        length input  -> mm
        spacing input -> micrometers (um)
    Internal storage:
        meters (SI units)
    """

    def __init__(self, width_mm, height_mm, dx_um, dy_um=None):
        """
        Parameters
        ----------
        width_mm : float
            Domain width in mm
        height_mm : float
            Domain height in mm
        dx_um : float
            Pixel spacing in x direction (micrometers)
        dy_um : float or None
            Pixel spacing in y direction
            If None, dy = dx
        """

        self.width_mm = width_mm
        self.height_mm = height_mm

        self.dx_um = dx_um
        self.dy_um = dy_um if dy_um is not None else dx_um

        # Convert to meters
        self.width_m = width_mm * 1e-3
        self.height_m = height_mm * 1e-3
        self.dx_m = self.dx_um * 1e-6
        self.dy_m = self.dy_um * 1e-6

        # Number of grid points
        self.nx = int(np.round(self.width_m / self.dx_m))
        self.ny = int(np.round(self.height_m / self.dy_m))

        # Coordinate vectors centered at origin
        self.x = np.linspace(
            -self.width_m / 2,
            self.width_m / 2,
            self.nx
        )

        self.y = np.linspace(
            -self.height_m / 2,
            self.height_m / 2,
            self.ny
        )

        # Meshgrid
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def shape(self):
        """Return grid shape."""
        return (self.ny, self.nx)

    def summary(self):
        """Print grid summary."""
        print("=== Simulation Grid ===")
        print(f"Width      : {self.width_mm} mm")
        print(f"Height     : {self.height_mm} mm")
        print(f"dx         : {self.dx_um} um")
        print(f"dy         : {self.dy_um} um")
        print(f"Grid shape : {self.ny} x {self.nx}")

    def create_field(self, initial_value=0.0):
        """
        Create empty field on grid.

        Returns
        -------
        np.ndarray
        """
        return np.full((self.ny, self.nx), initial_value, dtype=float)