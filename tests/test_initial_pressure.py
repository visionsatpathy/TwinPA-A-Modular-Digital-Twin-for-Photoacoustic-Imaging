from core.grid import SimulationGrid
from core.materials import MaterialLibrary
from digital_twin.phantom.geometry import PhantomBuilder
from digital_twin.phantom.tissue_map import TissuePropertyMap
from digital_twin.optical_model.fluence_solver import DiffusionFluenceSolver
from digital_twin.pressure_model.initial_pressure import InitialPressureSolver

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

fluence_solver = DiffusionFluenceSolver(grid)
fluence = fluence_solver.solve(
    mu_a=MaterialLibrary.MUSCLE.mu_a,
    mu_s=MaterialLibrary.MUSCLE.mu_s
)

pressure_solver = InitialPressureSolver(
    gruneisen=MaterialLibrary.MUSCLE.gruneisen
)

p0 = pressure_solver.compute(
    property_map.mu_a,
    fluence
)

print("Pressure shape:", p0.shape)
print("Background pressure:", p0[0, 0])
print("Center pressure:", p0[400, 400])
print("Max pressure:", p0.max())