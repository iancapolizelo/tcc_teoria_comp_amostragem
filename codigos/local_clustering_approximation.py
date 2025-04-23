import networkx as nx
from math import log, floor, ceil
import random
import operator
import collections

def local_clustering_approximation(G: nx.classes.graph.Graph, epsilon: float, delta: float, p: float, f: str):
    """
    Approximates the local clustering coefficient of a graph.

    Args:
        G: The graph to approximate the local clustering coefficient for.
        epsilon: The error tolerance.
        delta: The probability of failure.
        p: The probability of sampling an edge.

    Returns:
        The approximated local clustering coefficient.
    """
    #parameters
    local_clustering = {}
    t_aprox = {}
    m = G.number_of_edges()
    max_degree = max(G.degree, key=operator.itemgetter(1))[1]
    universalConstant=0.5

    for v in G.nodes():
      t_aprox[v] = 0

    r = ceil((universalConstant / (epsilon * epsilon * p)) * (((floor(log(max_degree, 2.0) - 1.0) + 1.0) * log(1/p))+ log(1/delta)))

    print("Number of samples r = " + str(r),file=f)

    for i in range(r):
      a, b = random.choice(list(G.edges()))

      for v in G.neighbors(a):

        if v in list(G.neighbors(b)):
          t_aprox[v] = t_aprox[v] + (m/r)

        if G.degree(v) > 1:
          local_clustering[v] = round(((2 * t_aprox[v]) / (G.degree(v) * (G.degree(v) - 1))),2)
        else:
          local_clustering[v] = 0

    return local_clustering