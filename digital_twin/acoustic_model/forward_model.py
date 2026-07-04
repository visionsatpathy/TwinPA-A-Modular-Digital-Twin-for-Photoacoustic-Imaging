import numpy as np
from digital_twin.acoustic_model.detector_response import DetectorResponse


class AcousticForwardModel:
    """
    Forward acoustic model with detector impulse response.
    """

    def __init__(
        self,
        grid,
        detector_array,
        acquisition,
        speed_of_sound=1540,
        center_frequency_mhz=5
    ):
        self.grid = grid
        self.detector_array = detector_array
        self.acquisition = acquisition
        self.speed_of_sound = speed_of_sound

        response = DetectorResponse(
            center_frequency_mhz=center_frequency_mhz,
            sampling_dt=acquisition.dt_s
        )

        self.impulse_response = response.generate_impulse_response()

    def simulate(self, p0):
        num_detectors = self.detector_array.num_detectors
        num_samples = self.acquisition.num_samples

        sinogram = np.zeros((num_detectors, num_samples))

        x_coords = self.grid.x
        y_coords = self.grid.y
        pulse_len = len(self.impulse_response)

        for iy, y in enumerate(y_coords):
            for ix, x in enumerate(x_coords):

                amplitude = p0[iy, ix]

                if amplitude <= 0:
                    continue

                for det_idx, detector in enumerate(self.detector_array.positions):

                    dx = detector[0] - x
                    dy = detector[1] - y
                    distance = np.sqrt(dx**2 + dy**2)

                    # geometric spreading (2D approximation)
                    spread = 1 / np.sqrt(distance + 1e-12)

                    arrival_time = distance / self.speed_of_sound
                    sample_idx = int(arrival_time / self.acquisition.dt_s)

                    start = sample_idx
                    end = sample_idx + pulse_len

                    if end < num_samples:
                        sinogram[det_idx, start:end] += (
                            amplitude
                            * spread
                            * self.impulse_response
                        )

        return sinogram