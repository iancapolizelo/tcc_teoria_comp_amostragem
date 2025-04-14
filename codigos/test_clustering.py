import random
import networkx as nx
import time
import os
import collections
from random import sample, choice
from math import log, floor, ceil
import itertools
import sys
from statistics import stdev 
from local_clustering_approximation import local_clustering_approximation

###########################################################################################
def read_snap_graph(file: str):
    """
    Function that reads a graph from file


    Parameters
    -------------
    file: string
        Path to the input graph file
    
    directed: int
        Binary flag indicating that G is directed (if 1) or not (if 0)


    Returns
    -------------
    G: nx.classes.graph.Graph
        NetworkX graph

    """

    G = nx.read_edgelist(file)

    return G
###########################################################################################

def calcular_media_dicionario(dicionario):
  """Calcula a média dos valores de um dicionário.

  Args:
    dicionario: O dicionário para calcular a média.

  Returns:
    A média dos valores do dicionário.
  """
  valores = list(dicionario.values())
  media = sum(valores) / len(valores) if valores else 0  # Evite ZeroDivisionError se o dicionário estiver vazio
  return media

###########################################################################################
def main(in_file: str, out_file: str):

    """
    Main function


    Parameters
    -------------
    file: string
        Path to the input graph file

    directed: int
        Binary flag indicating that G is directed (if 1) or not (if 0)
  
    """


    '''
    Barabasi-Albert graph generator
    n = 1000
    #G = nx.barabasi_albert_graph(n, 3)
    '''

    with open(in_file, 'r') as f:
        G = read_snap_graph(f)
    f.close
    n = len(G)

    with open(out_file, 'w') as f:
        print("###########################################################################################", file=f)
        print("New round of tests: \n", file=f)
        print("The graph has {} vertices and {} edges".format(G.number_of_nodes(), G.number_of_edges()), file=f)


        t1 = time.process_time()
        pc = nx.clustering(G)
        pc_ord = dict(sorted(pc.items()))
        print("Total running time (exact algorithm): " + str(time.process_time() - t1), file=f)
        print("Exact coefficient clustering values: \n" + ', '.join('{:0.20f}'.format(pc_ord[i]) for i in pc_ord) + "\n", file=f)


        epsilon = [0.04, 0.06, 0.08, 0.10]
        delta = 0.1
        p = 0.1

        i = 0
        for e in epsilon:
            times = []
            errors = []
            diffs_list = []
            deviations = []
            while i < 10:
                print("", file=f)
                print("Iteration: " + str(i), file=f)
                print("epsilon: "+str(e)+" ------------------------------------", file=f)
                t2 = time.process_time()
                pc_tilde = local_clustering_approximation(G, float(e), float(delta), float(p), f)
                pc_tilde_ord = dict(sorted(pc_tilde.items()))
                print("Total running time (approximation algorithm): " + str(time.process_time() - t2), file=f)
                times.append(time.process_time() - t2)
                print("Approximated coefficient clustering values: \n" + ', '.join('{:0.20f}'.format(pc_tilde_ord[i]) for i in pc_tilde_ord), file=f)
                print("Zeros = " + str(list(pc_tilde_ord.values()).count(0)), file=f)
                print("Average = " + str(calcular_media_dicionario(pc_tilde_ord)) + "\n", file=f)

                diffs = {}
                sum_diffs = 0.0
                for v in G.nodes:
                    diffs[v] = abs(pc_ord[v] - pc_tilde_ord[v])
                    sum_diffs += diffs[v]
                    diffs_list.append(diffs[v])
                avg_error = sum_diffs/len(G.nodes)
                errors.append(avg_error)
                deviation = stdev(diffs_list)
                deviations.append(deviation)
        
                print("Absolute difference between the exact and the approximation algorithm:\n" + ', '.join('{:0.20f}'.format(diffs[i]) for i in diffs), file=f)
                sorted_diffs = sorted(diffs.items(), key=lambda kv: kv[1], reverse=True)
                diffs_d = collections.OrderedDict(sorted_diffs)
                print("Absolute difference between the exact and the approximation algorithm (sorted, non-increasing):\n" + ', '.join('{:0.20f}'.format(diffs_d[i]) for i in diffs_d), file=f)

                i += 1
            print("", file=f)
            print("", file=f)
            print("time: ", file=f)
            print(times, file=f)
            print("avg error: ", file=f)
            print(errors, file=f)
            print("std dev: ", file=f)
            print(deviations, file=f)
        
            i = 0
    f.close
    del G
###########################################################################################

###########################################################################################
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Use: python3.7 test_clustering.py <path_to_file> <out_file>.")

    main(sys.argv[1], sys.argv[2])
###########################################################################################