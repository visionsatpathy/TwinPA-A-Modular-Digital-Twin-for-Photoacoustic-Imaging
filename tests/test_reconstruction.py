from core.grid import SimulationGrid
from digital_twin.phantom.geometry import PhantomBuilder
from digital_twin.acoustic_model.detector_array import CircularDetectorArray
from digital_twin.acoustic_model.acquisition import AcquisitionSystem
from digital_twin.acoustic_model.forward_model import AcousticForwardModel
from reconstruction.delay_and_sum import DelayAndSumReconstructor
from visualization.plotting import OAPlotter

grid = SimulationGrid(10, 10, 200)

phantom = PhantomBuilder(grid)

# IMPORTANT: use off-center target
phantom.add_circle(2, -1, 1, 1)

ground_truth = phantom.get_mask() * 10

detectors = CircularDetectorArray(
    radius_mm=8,
    num_detectors=64
)

daq = AcquisitionSystem(
    sampling_frequency_mhz=40,
    duration_us=20
)

forward_model = AcousticForwardModel(
    grid,
    detectors,
    daq
)

sinogram = forward_model.simulate(ground_truth)

reconstructor = DelayAndSumReconstructor(
    grid,
    detectors,
    daq
)

reconstructed = reconstructor.reconstruct(sinogram)

OAPlotter.show_image(
    ground_truth,
    title="Ground Truth",
    cmap="viridis"
)

OAPlotter.show_sinogram(sinogram)

OAPlotter.show_image(
    reconstructed,
    title="Reconstructed Image",
    cmap="hot"
)