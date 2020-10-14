import numpy as np
from lab8.pso_particle import Particle
import matplotlib.pyplot as plt
# Import PySwarms
from lab8.pso_rastrigin import error, grad_error
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher
from matplotlib import animation, rc

from IPython.display import HTML
class PSO:
    w = 0.729
    c1 = 1.49445
    c2 = 1.49445
    lr = 0.01

    def __init__(self, dims, numOfBoids, numOfEpochs):
        self.swarm_list = [Particle(dims, -500, 500) for i in range(numOfBoids)]
        self.numOfEpochs = numOfEpochs

        self.best_swarm_position = np.random.uniform(low=-500, high=500, size=dims)
        self.best_swarm_error = 1e80  # Set high value to best swarm error best swarm error

    def optimize(self):
        for i in range(self.numOfEpochs):

            for j in range(len(self.swarm_list)):

                current_particle = self.swarm_list[j]  # get current particle

                Vcurr = grad_error(current_particle.position)  # calculate current velocity of the particle

                deltaV = self.w * Vcurr \
                         + self.c1 * (current_particle.best_part_pos - current_particle.position) \
                         + self.c2 * (self.best_swarm_position - current_particle.position)  # calculate delta V

                new_position = self.swarm_list[j].position - self.lr * deltaV  # calculate the new position

                self.swarm_list[j].setPos(new_position)  # update the position of particle

                if error(new_position) < self.best_swarm_error:  # check the position if it's best for swarm
                    self.best_swarm_position = new_position
                    self.best_swarm_error = error(new_position)

            print('Epoch: {0} | Best position: [{1},{2}] | Best known error: {3}'.format(i,
                                                                                         self.best_swarm_position[0],
                                                                                         self.best_swarm_position[1],
                                                                                         self.best_swarm_error))
            return self.best_swarm_position[0],self.best_swarm_position[1],self.best_swarm_error


if __name__ == "__main__":
    pso = PSO(dims=2, numOfBoids=30, numOfEpochs=500)
    results = pso.optimize()
    m = Mesher(func=fx.sphere)
    options = {'c1': 0.2, 'c2': 0.5, 'w': 0.9}

    optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=2, options=options)
    optimizer.optimize(fx.sphere, iters=100)
    pos_history_3d = m.compute_history_3d(optimizer.pos_history)

    # Make a designer and set the x,y,z limits to (-1,1), (-1,1) and (-0.1,1) respectively
    from pyswarms.utils.plotters.formatters import Designer
    d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)], label=['x-axis', 'y-axis', 'z-axis'])

    # Make animation
    pos_history_3d = m.compute_history_3d(optimizer.pos_history)  # preprocessing
    animation3d = plot_surface(pos_history=pos_history_3d,
                               mesher=m, designer=d,
                               mark=(0, 0, 0))
    animation3d.to_html5_video()
    pass
    pass