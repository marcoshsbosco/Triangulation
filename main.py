from calc import *


# setup -----------------------------------------

receptors = [
 Receptor(1.55, 17.63, 1.35, -26.0, 2.1),
 Receptor(-4.02, 0.00, 1.35, -33.8, 1.8),
 Receptor(-4.40, 9.60, 1.35, -29.8, 1.3),
 Receptor(9.27, 4.64, 1.35, -31.2, 1.4),
 Receptor(9.15, 12.00, 1.35, -33.0, 1.5)
]

e1 = Emitter(0.00, 9.00, 1.24)
signals_e1 = [-48.4, -50.6, -32.2, -47.4, -46.3]
e2 = Emitter(3.00, 3.00, 1.24)
signals_e2 = [-46.9, -46.4, -41.2, -45.8, -48.7]

# -----------------------------------------------

print("----- Caso 1 -----")

for i, receptor in enumerate(receptors):
	radial_distance(receptor, signals_e1[i])  # seta r para o emissor 1
	print(f"Distância radial de e1 para r{i + 1}: {receptor.r:.02f} m")

XY = solve_matrices(receptors)
e1.x_calc = XY[0, 0]
e1.y_calc = XY[1, 0]

print("\nDistância calculada para e1:")
print(f"x = {XY[0, 0]} m\ny = {XY[1, 0]} m")

plot(receptors, e1, caso=1)

# -----------------------------------------------

print("\n----- Caso 2 -----")

for i, receptor in enumerate(receptors):
	radial_distance(receptor, signals_e2[i])  # seta r para o emissor 2
	print(f"Distância radial de e2 para r{i + 1}: {receptor.r:.02f} m")

XY = solve_matrices(receptors)
e2.x_calc = XY[0, 0]
e2.y_calc = XY[1, 0]

print("\nDistância calculada para e1:")
print(f"x = {XY[0, 0]} m\ny = {XY[1, 0]} m")

plot(receptors, e2, caso=2)