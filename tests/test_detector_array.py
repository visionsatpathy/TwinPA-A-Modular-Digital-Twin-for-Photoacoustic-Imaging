from digital_twin.acoustic_model.detector_array import CircularDetectorArray

array = CircularDetectorArray(
    radius_mm=25,
    num_detectors=256
)

array.summary()

print("First detector:", array.positions[0])
print("Second detector:", array.positions[1])