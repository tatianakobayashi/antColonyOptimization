from sys import maxsize
from random import randrange, seed

# RO = 0.2
# TAUMAX = 2
RANDMAX = 32767
ALPHA = 0.5
BETA = 0.5
EVAPORATION_RATE = 0.6

class Graph:

    def __init__(self, f):
        seed(None)
        lines = f.readlines()

        # initializing variables
        self.numberOfNodes = int(lines[0])

        # get edges from file
        edges_int = [[int(val) for val in line.split()] for line in lines[1:]]

        self.bestLength = maxsize
        self.bestRoute = [-1 for x in range(self.numberOfNodes)]
        self.pheromones = [[0.0 for x in range(self.numberOfNodes)] for y in range(self.numberOfNodes)]
        self.deltaPheromones = [[0.0 for x in range(self.numberOfNodes)] for y in range(self.numberOfNodes)]
        self.edges = [[False for x in range(self.numberOfNodes)] for y in range(self.numberOfNodes)]
        self.bestRouteFitness = 0

        self.numberOfEdges = len(edges_int)

        for row in edges_int:
            # Insert edges
            self.edges[row[0]-1][row[1]-1] = self.edges[row[1]-1][row[0]-1] = True
            # Initialize pheromone trail
            self.pheromones[row[0]-1][row[1]-1] = self.pheromones[row[1]-1][row[0]-1] = randrange(RANDMAX)

    def updatePheromones(self):
        for i, j in self.pheromones:
            # Evaporate trail
            self.pheromones[i][j] = self.pheromones[i][j] * EVAPORATION_RATE
            # Reinforce trail
            inBestRoute = False
            for a in self.bestRoute:
                if a == i and self.bestRoute[self.bestRoute.index(a) + 1] == j:
                    inBestRoute = True
            if inBestRoute:
                newPheromones = (1 / self.bestRouteFitness) * BETA
            else:
                newPheromones = 0
            self.pheromones[i][j] = (1 - ALPHA) * self.pheromones[i][j] + ALPHA * newPheromones
            # self.deltaPheromones[i][j] = 0.0

    def exists(self, a, b):
        return self.edges[int(a)][int(b)]