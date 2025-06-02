import networkx as nx
from math import log, floor, ceil
import random

def local_clustering_approximation(G: nx.classes.graph.Graph, epsilon: float, delta: float, p: float, f: str, max_degree: int, m: int, universalConstant: float = 0.5, local_clustering: dict = None, t_aprox: dict = None):
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
    
    r = ceil((universalConstant / (epsilon * epsilon * p)) * (((floor(log(max_degree, 2.0) - 1.0) + 1.0) * log(1/p))+ log(1/delta)))

    if r > m:
      r = m
      print("r > m, entao r <- m " + str(r),file=f)

    print("Numero de amostras eh r = " + str(r),file=f)
    edges_list = list(G.edges())

    for i in range(r):
      a, b = random.choice(edges_list)

      for v in G.neighbors(a):
        grau_v = G.degree(v)

        if v in list(G.neighbors(b)):
          t_aprox[v] = t_aprox[v] + (m/r)

        if grau_v > 1:
          local_clustering[v] = round(((2 * t_aprox[v]) / (grau_v * (grau_v - 1))),2)

    return local_clustering



def local_clustering_exato(G: nx.classes.graph.Graph, f: str):
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

    for v in G.nodes():
      t_aprox[v] = 0
      local_clustering[v] = 0

    for i in G.edges():
      a, b = i

      for v in G.neighbors(a):
        grau_v = G.degree(v)

        if v in list(G.neighbors(b)):
          t_aprox[v] = t_aprox[v] + 1

        if grau_v > 1:
          local_clustering[v] = round(((2 * t_aprox[v]) / (grau_v * (grau_v - 1))),2)

    return local_clustering
