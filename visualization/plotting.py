import matplotlib.pyplot as plt
import numpy as np


class OAPlotter:
    """
    Visualization utilities for optoacoustic simulations.
    """

    @staticmethod
    def show_image(image, title="Image", cmap="viridis"):
        plt.figure(figsize=(6, 5))
        plt.imshow(image, cmap=cmap)
        plt.colorbar()
        plt.title(title)
        plt.xlabel("X pixels")
        plt.ylabel("Y pixels")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def show_sinogram(sinogram):
        plt.figure(figsize=(8, 5))
        plt.imshow(
            sinogram,
            aspect="auto",
            cmap="hot"
        )
        plt.colorbar(label="Amplitude")
        plt.title("Optoacoustic Sinogram")
        plt.xlabel("Time samples")
        plt.ylabel("Detector index")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def show_trace(sinogram, detector_index=0):
        trace = sinogram[detector_index]

        plt.figure(figsize=(8, 4))
        plt.plot(trace)
        plt.title(f"Detector Trace #{detector_index}")
        plt.xlabel("Time sample")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.tight_layout()
        plt.show()