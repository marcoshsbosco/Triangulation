import numpy as np
import matplotlib.pyplot as plt

class Receptor:
	def __init__(self, x, y, z, p_ref, atten):
		self.x = x
		self.y = y
		self.z = z
		self.p_ref = p_ref
		self.atten = atten
		self.r = None

class Emitter:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

def radial_distance(receptor, power):
	receptor.r = 10 ** ((receptor.p_ref - power) / (10 * receptor.atten))

def solve_matrices(receptors):
	for receptor in receptors:
		receptor.w = receptor.r ** 2 - receptor.x ** 2 - receptor.y ** 2

	A = 2 * np.matrix([[receptors[4].x - receptors[0].x, receptors[4].y - receptors[0].y],
					   [receptors[4].x - receptors[1].x, receptors[4].y - receptors[1].y],
					   [receptors[4].x - receptors[2].x, receptors[4].y - receptors[2].y],
					   [receptors[4].x - receptors[3].x, receptors[4].y - receptors[3].y]])
				   
	B = np.matrix([[receptors[0].w - receptors[4].w],
				   [receptors[1].w - receptors[4].w],
				   [receptors[2].w - receptors[4].w],
				   [receptors[3].w - receptors[4].w]])
				   
	XY = np.linalg.inv(np.transpose(A) * A) * np.transpose(A) * B

	return XY

def plot(receptors, emitter, caso):
	figure, axes = plt.subplots(figsize=(16, 9))
	plt.axis([-20, 30, -10, 30])
	axes.set_aspect(1)
	axes.set_title(f"Caso {caso}")
	axes.set_xlabel("x (m)")
	axes.set_ylabel("y (m)")
	
	axes.plot(emitter.x_calc, emitter.y_calc, 'ro', label="Posição calculada")
	axes.plot(emitter.x, emitter.y, 'go', label="Posição real")
	
	for i, receptor in enumerate(receptors):
		axes.plot(receptor.x, receptor.y, 'bo', label="Receptor" if not i else None)
		
		circle = plt.Circle((receptor.x, receptor.y), receptor.r, fill=False)
		axes.add_artist(circle)
	
	axes.legend()
	
	plt.savefig(f"{int(emitter.x)} {int(emitter.y)}.png")