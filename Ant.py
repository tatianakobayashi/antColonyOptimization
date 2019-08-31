from random import seed, random, randrange

ALPHA = 0.5
Q = 80.0

class Ant:
    def eraseRoute(self):
        for i in range(0, self.graph.numberOfNodes):
          self.route[i] = -1

    def __init__(self, graph):
        self.graph = graph

        self.route = [-1 for x in range(graph.numberOfNodes)]

        self.routeLenght = 0

        self.probabilities = [[0.0 for x in range(self.graph.numberOfEdges)] for y in range(self.graph.numberOfEdges)]

        seed(a=None)


    def visited(self, node):
        for r in self.route:
          if r == node:
            return True
        return False

    def updatePheromones(self):
        for r in range(0, self.graph.numberOfNodes - 1):
          self.graph.deltaPheromones[self.route[r]][self.route[r+1]] += Q
          self.graph.deltaPheromones[self.route[r+1]][self.route[r]] += Q

    def valid(self):
        # for i in range(0, self.graph.numberOfNodes - 1):
        #     node_a = self.route[i]
        #     node_b = self.route[i+1]
        #
        #     if node_a < 0 or node_b < 0:
        #         return -1
        #
        #     if not self.graph.exists(node_a, node_b):
        #         return -2
        #
        #     for j in range(0, i-1):
        #         if self.route[i] == self.route[j]:
        #              return -3
        #
        # if not self.graph.exists(self.FIRST_NODE, self.route[self.graph.numberOfNodes-1]):
        #     return -4
        #
        # return 0
        for i in range(0, len(self.route)):
            if i + 1 == len(self.route):
                if not self.graph.exists(self.route[i], 0):
                    return False
            else:
                if not self.graph.exists(self.route[i], self.route[i+1]):
                    return False
        return True

    def chosePath(self):
        self.route[0] = randrange(0, self.graph.numberOfNodes)

        for i in range(1, self.graph.numberOfNodes - 1):
            # cityi = self.route[i]
            # count = 0
            # for c in range (0, self.graph.numberOfNodes):
            #   if cityi == c:
            #     continue
            #
            #   if self.graph.exists(cityi, c):
            #     if not self.visited(c):
            #       self.probabilities[count][0] = self.phi(cityi, c)
            #       self.probabilities[count][1] = c
            #       count+=1
            # if 0 == count:
            #   return
            #
            # self.route[i + 1] = int(self.probs())
            # while not self.visited(self.route[i + 1]):
            #   self.route[i+1] += 1
            # self.routeLenght += 1
            while(not self.visited(self.route[i])):
                newStop = randrange(0, self.graph.numberOfNodes)
                if self.graph.exists(self.route[i-1], self.route[i]):
                    self.route[i] = newStop
        for i in range (0, self.graph.numberOfNodes):
            if not self.visited(i):
                self.route[-1] = i

    def phi(self, node_a, node_b):
        tau = self.graph.pheromones[int(node_a)][int(node_b)] ** ALPHA

        soma = 0.0
        for c in range (0, self.graph.numberOfNodes):
            if self.graph.exists(node_a, c):
              if not self.visited(c):
                soma += self.graph.pheromones[int(node_a)][int(c)] ** ALPHA

        return tau / soma

    def probs(self):
        xi = random()
        i = 0
        soma = 0.0

        while (soma < xi):
            soma += self.probabilities[i][0]
            i+=1

        return soma #probabilities[i][1]

    def route_str(self):
        return 'Rota: ' + str(self.route)
  # friend class Application
