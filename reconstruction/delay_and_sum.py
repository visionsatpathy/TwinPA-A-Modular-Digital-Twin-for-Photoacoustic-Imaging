import numpy as np


class DelayAndSumReconstructor:
    """
    Delay-and-sum reconstruction for circular detector arrays.
    """

    def __init__(self, grid, detector_array, acquisition, speed_of_sound=1540):
        self.grid = grid
        self.detector_array = detector_array
        self.acquisition = acquisition
        self.speed_of_sound = speed_of_sound

    def reconstruct(self, sinogram):
        image = np.zeros(self.grid.shape())

        x_coords = self.grid.x
        y_coords = self.grid.y

        for iy, y in enumerate(y_coords):
            for ix, x in enumerate(x_coords):

                pixel_sum = 0.0

                for det_idx, detector in enumerate(self.detector_array.positions):

                    dx = detector[0] - x
                    dy = detector[1] - y

                    distance = np.sqrt(dx**2 + dy**2)

                    arrival_time = distance / self.speed_of_sound
                    sample_idx = int(arrival_time / self.acquisition.dt_s)

                    if sample_idx < sinogram.shape[1]:
                        pixel_sum += sinogram[det_idx, sample_idx]

                image[iy, ix] = pixel_sum

        return image