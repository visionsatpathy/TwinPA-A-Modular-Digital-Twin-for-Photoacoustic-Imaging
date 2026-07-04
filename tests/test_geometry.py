from core.grid import SimulationGrid
from digital_twin.phantom.geometry import PhantomBuilder

grid = SimulationGrid(40, 40, 50)

phantom = PhantomBuilder(grid)
phantom.add_circle(
    center_x_mm=0,
    center_y_mm=0,
    radius_mm=2,
    value=1
)

mask = phantom.get_mask()

print("Phantom shape:", mask.shape)
print("Max value:", mask.max())
print("Feature pixels:", (mask > 0).sum())