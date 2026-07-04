from digital_twin.acoustic_model.detector_response import DetectorResponse
import matplotlib.pyplot as plt

response = DetectorResponse(
    center_frequency_mhz=5,
    bandwidth=0.8,
    sampling_dt=25e-9
)

impulse = response.generate_impulse_response()

print("Impulse length:", len(impulse))
print("Max amplitude:", impulse.max())
print("Min amplitude:", impulse.min())

plt.plot(impulse)
plt.title("Detector Impulse Response")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()