from core.grid import SimulationGrid
from digital_twin.phantom.geometry import PhantomBuilder
from digital_twin.acoustic_model.detector_array import CircularDetectorArray
from digital_twin.acoustic_model.acquisition import AcquisitionSystem
from digital_twin.acoustic_model.forward_model import AcousticForwardModel
from visualization.plotting import OAPlotter

grid = SimulationGrid(10, 10, 200)

phantom = PhantomBuilder(grid)
phantom.add_circle(0, 0, 1, 1)

p0 = phantom.get_mask() * 10

detectors = CircularDetectorArray(
    radius_mm=8,
    num_detectors=64
)

daq = AcquisitionSystem(
    sampling_frequency_mhz=40,
    duration_us=20
)

model = AcousticForwardModel(
    grid,
    detectors,
    daq
)

sinogram = model.simulate(p0)

OAPlotter.show_image(
    p0,
    title="Initial Pressure Map",
    cmap="viridis"
)

OAPlotter.show_sinogram(sinogram)

OAPlotter.show_trace(
    sinogram,
    detector_index=0
)