from digital_twin.acoustic_model.acquisition import AcquisitionSystem

daq = AcquisitionSystem(
    sampling_frequency_mhz=40,
    duration_us=50
)

daq.summary()

print("First time sample:", daq.time_axis[0])
print("Last time sample:", daq.time_axis[-1])