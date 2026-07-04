import numpy as np


class AcquisitionSystem:
    """
    Acquisition parameters for optoacoustic detector signals.
    """

    def __init__(self, sampling_frequency_mhz, duration_us):
        self.sampling_frequency_mhz = sampling_frequency_mhz
        self.duration_us = duration_us

        self.dt_s = 1 / (sampling_frequency_mhz * 1e6)
        self.num_samples = int(
            duration_us * 1e-6 / self.dt_s
        )

        self.time_axis = np.arange(self.num_samples) * self.dt_s

    def summary(self):
        print("=== Acquisition System ===")
        print("Sampling frequency (MHz):", self.sampling_frequency_mhz)
        print("Duration (us):", self.duration_us)
        print("Time step (s):", self.dt_s)
        print("Samples:", self.num_samples)