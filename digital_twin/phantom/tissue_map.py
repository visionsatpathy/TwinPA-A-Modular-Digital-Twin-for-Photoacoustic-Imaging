import numpy as np


class TissuePropertyMap:
    def __init__(self, grid, background_material):
        self.grid = grid

        shape = grid.shape()

        self.mu_a = np.full(shape, background_material.mu_a)
        self.mu_s = np.full(shape, background_material.mu_s)
        self.speed_of_sound = np.full(shape, background_material.speed_of_sound)
        self.density = np.full(shape, background_material.density)

    def assign_material(self, mask, material):
        region = mask > 0

        self.mu_a[region] = material.mu_a
        self.mu_s[region] = material.mu_s
        self.speed_of_sound[region] = material.speed_of_sound
        self.density[region] = material.density