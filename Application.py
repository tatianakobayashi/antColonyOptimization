from Graph import Graph
from Ant import Ant

NUMBER_OF_ANTS = 100
EXECS = 10

class Application:
    def __init__(self, f):
        self.graph = Graph(f)

        self.ants = [Ant(self.graph) for x in range(NUMBER_OF_ANTS)]

    def run(self):
        print('Start run')
        for iterations in range(1, EXECS):
            print('Iteration #' + str(iterations))
            for ant in self.ants:
                print('Ant #' + str(self.ants.index(ant)))
                while not ant.valid():
                    ant.eraseRoute()
                    ant.chosePath()

                print('Ant #' + str(self.ants.index(ant)) + ' ' + ant.route_str())

                rlength = ant.routeLenght
                if (rlength < self.graph.bestLength):
                    self.graph.bestLength = rlength
                    self.graph.bestRouteFitness = 1/rlength
                    for i in range(0, self.graph.numberOfNodes):
                        self.graph.bestRoute[i] = ant.route[i]

                        self.updatePheromones()

            for ant in self.ants:
                ant.eraseRoute()
                self.print_results()

    def updatePheromones(self):
        for ant in self.ants:
            ant.updatePheromones()
            self.graph.updatePheromones()

    def print_results(self):
        print('Best route: ' + str(self.bestRoute))
        print('Best length: ' + str(self.graph.bestLength))