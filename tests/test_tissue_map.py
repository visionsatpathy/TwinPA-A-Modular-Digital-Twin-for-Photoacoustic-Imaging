from core.grid import SimulationGrid
from core.materials import MaterialLibrary
from digital_twin.phantom.geometry import PhantomBuilder
from digital_twin.phantom.tissue_map import TissuePropertyMap

grid = SimulationGrid(40, 40, 50)

phantom = PhantomBuilder(grid)
phantom.add_circle(0, 0, 2, 1)

mask = phantom.get_mask()

property_map = TissuePropertyMap(
    grid,
    background_material=MaterialLibrary.MUSCLE
)

property_map.assign_material(
    mask,
    MaterialLibrary.BLOOD
)

print("Background absorption:", property_map.mu_a[0, 0])
print("Center absorption:", property_map.mu_a[400, 400])