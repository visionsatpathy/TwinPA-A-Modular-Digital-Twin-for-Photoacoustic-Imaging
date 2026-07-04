import numpy as np


class DetectorResponse:
    """
    Models detector impulse response.
    Gaussian-modulated sinusoidal pulse.
    """

    def __init__(
        self,
        center_frequency_mhz=5,
        bandwidth=0.8,
        sampling_dt=25e-9
    ):
        self.center_frequency_hz = center_frequency_mhz * 1e6
        self.bandwidth = bandwidth
        self.dt = sampling_dt

    def generate_impulse_response(self):
        pulse_duration = 2 / self.center_frequency_hz

        t = np.arange(
            -pulse_duration,
            pulse_duration,
            self.dt
        )

        sigma = pulse_duration / (2 * self.bandwidth)

        envelope = np.exp(-(t ** 2) / (2 * sigma ** 2))

        carrier = np.sin(
            2 * np.pi * self.center_frequency_hz * t
        )

        impulse_response = envelope * carrier

        max_val = np.max(np.abs(impulse_response))
        if max_val > 0:
            impulse_response /= max_val

        return impulse_response