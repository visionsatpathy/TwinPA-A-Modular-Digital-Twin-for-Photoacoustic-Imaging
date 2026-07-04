from core.grid import SimulationGrid
from core.materials import MaterialLibrary
from digital_twin.optical_model.fluence_solver import DiffusionFluenceSolver

grid = SimulationGrid(40, 40, 50)

solver = DiffusionFluenceSolver(grid)

muscle = MaterialLibrary.MUSCLE

fluence = solver.solve(
    mu_a=muscle.mu_a,
    mu_s=muscle.mu_s
)

print("Shape:", fluence.shape)
print("Top:", fluence[0, 0])
print("Bottom:", fluence[-1, 0])