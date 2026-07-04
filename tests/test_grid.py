from core.grid import SimulationGrid

grid = SimulationGrid(
    width_mm=40,
    height_mm=40,
    dx_um=50
)

grid.summary()

field = grid.create_field()
print(field.shape)