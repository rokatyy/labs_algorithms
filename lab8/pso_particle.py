from lab8.pso_rastrigin import error
import numpy as np

class Particle:

    def __init__(self, dim, minx, maxx):
        self.position = np.random.uniform(low=minx, high=maxx, size=dim)
        self.velocity = np.random.uniform(low=minx, high=maxx, size=dim)
        self.best_part_pos = self.position.copy()

        self.error = error(self.position)
        self.best_part_err = self.error.copy()

    def setPos(self, pos):
        self.position = pos
        self.error = error(pos)
        if self.error < self.best_part_err:
            self.best_part_err = self.error
            self.best_part_pos = pos