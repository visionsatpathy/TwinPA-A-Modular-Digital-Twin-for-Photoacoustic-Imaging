import numpy as np


class CircularDetectorArray:
    """
    Circular detector array.
    Input radius in mm.
    Internal coordinates stored in meters.
    """

    def __init__(self, radius_mm, num_detectors):
        self.radius_mm = radius_mm
        self.radius_m = radius_mm * 1e-3

        self.num_detectors = num_detectors
        self.positions = self._generate_positions()

    def _generate_positions(self):
        positions = []

        angles = np.linspace(
            0,
            2 * np.pi,
            self.num_detectors,
            endpoint=False
        )

        for theta in angles:
            x = self.radius_m * np.cos(theta)
            y = self.radius_m * np.sin(theta)

            positions.append((x, y))

        return np.array(positions)

    def summary(self):
        print("=== Circular Detector Array ===")
        print("Radius (mm):", self.radius_mm)
        print("Radius (m):", self.radius_m)
        print("Detector count:", self.num_detectors)
        print("Position array shape:", self.positions.shape)