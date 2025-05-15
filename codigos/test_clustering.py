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
from local_clustering_approximation import local_clustering_approximation, local_clustering_exato

###########################################################################################
def read_graph(file_path, directed=False):
    with open(file_path, 'r') as f:
        if directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        for line in f:
            # Ignorar linhas de metadados que começam com '%'
            if line.startswith('%'):
                continue

            # Dividir a linha em tokens
            tokens = line.split()
            if len(tokens) >= 2:
                source = tokens[0]
                target = tokens[1]

                # Verificar se há um peso especificado
                if len(tokens) > 2:
                    weight = float(tokens[2])
                else:
                    weight = random.uniform(1, 100)  # Peso aleatório

                # Adicionar a aresta ao grafo
                G.add_edge(source, target, weight=weight)

    return G
###########################################################################################
def gerar_grafo_aleatorio(num_vertices, num_arestas):
    """Gera um grafo aleatório com o número especificado de vértices e arestas.

    Args:
        num_vertices: O número de vértices no grafo.
        num_arestas: O número de arestas no grafo.

    Returns:
        Um grafo aleatório.
    """
    G = nx.gnm_random_graph(num_vertices, num_arestas)
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
def main(in_file: str, out_file: str,  directed: int, aleatorio: int = 0):

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
    #G = gerar_grafo_aleatorio(90, 300)
    G = read_graph(in_file, directed)

    with open(out_file, 'w') as f:
        print("###########################################################################################", file=f)
        print("Nova rodada de testes: \n", file=f)
        print("O grafo tem {} vertices e {} arestas".format(G.number_of_nodes(), G.number_of_edges()), file=f)


        
        t1 = time.process_time()
        clustering_exato_networkx = nx.clustering(G)
        print("Total de tempo de execucao do algoritmo exato (lib networkx): " + str(time.process_time() - t1), file=f)
        #print("Exact coefficient clustering values: \n" + ', '.join('{:0.20f}'.format(pc_ord[i]) for i in pc_ord) + "\n", file=f)
        media_exato_networkx = calcular_media_dicionario(clustering_exato_networkx)
        print("Media dos coeficientes de clustering local do algoritmo exato (lib networkx) = " + str(media_exato_networkx) + "\n", file=f)
        exato_networkx_ord = dict(sorted(clustering_exato_networkx.items()))
        #print("Valores de coeficientes de clustering exato (lib networkx): ", file=f)
        #print(exato_networkx_ord, file=f)

        t1 = time.process_time()
        clustering_exato_nosso = local_clustering_exato(G, f)
        print("Total de tempo de execucao do algoritmo exato (autoral): " + str(time.process_time() - t1), file=f)
        #print("Exact coefficient clustering values: \n" + ', '.join('{:0.20f}'.format(pc_ord[i]) for i in pc_ord) + "\n", file=f)
        media_exato_nosso = calcular_media_dicionario(clustering_exato_nosso)
        print("Media dos coeficientes de clustering local do algoritmo exato (autoral) = " + str(media_exato_nosso) + "\n", file=f)
        exato_nosso_ord = dict(sorted(clustering_exato_nosso.items()))
        #print("Valores de coeficientes de clustering exato (autoral): ", file=f)
        #print(exato_nosso_ord, file=f)
        


        epsilon = [0.04, 0.06, 0.08, 0.10]
        delta = 0.1
        p = 0.1

        i = 0
        for e in epsilon:
            times = []
            errors_networkx = []
            errors_nosso = []
            diffs_list_networkx = []
            diffs_list_nosso = []
            deviations_networkx = []
            deviations_nosso = []
            while i < 10:
                print("", file=f)
                print("Iteracao: " + str(i), file=f)
                print("epsilon: "+str(e)+" ------------------------------------", file=f)
                t2 = time.process_time()
                pc_tilde = local_clustering_approximation(G, float(e), float(delta), float(p), f)
                print("Total de tempo de execucao do algoritmo de aproximacao: " + str(time.process_time() - t2), file=f)
                times.append(time.process_time() - t2)
                #print("Approximated coefficient clustering values: \n" + ', '.join('{:0.20f}'.format(pc_tilde_ord[i]) for i in pc_tilde_ord), file=f)
                print("Quantidade de Zeros = " + str(list(pc_tilde.values()).count(0)), file=f)
                avg_tilde = calcular_media_dicionario(pc_tilde)
                print("Media dos coeficientes de clustering local do algoritmo aproximado = " + str(avg_tilde) + "\n", file=f)
                pc_tilde_ord = dict(sorted(pc_tilde.items()))

                diffs_networkx = {}
                sum_diffs_networkx = 0.0

                diffs_nosso = {}
                sum_diffs_nosso = 0.0

                for v in G.nodes:
                    diffs_networkx[v] = abs(exato_networkx_ord[v] - pc_tilde_ord[v])
                    diffs_nosso[v] = abs(exato_nosso_ord[v] - pc_tilde_ord[v])
                    sum_diffs_networkx += diffs_networkx[v]
                    sum_diffs_nosso += diffs_nosso[v]
                    diffs_list_networkx.append(diffs_networkx[v])
                    diffs_list_nosso.append(diffs_nosso[v])
                avg_error_networkx = sum_diffs_networkx/len(G.nodes)
                avg_error_nosso = sum_diffs_nosso/len(G.nodes)
                errors_networkx.append(avg_error_networkx)
                errors_nosso.append(avg_error_nosso)
                deviation_networkx = stdev(diffs_list_networkx)
                deviation_nosso = stdev(diffs_list_nosso)
                deviations_networkx.append(deviation_networkx)
                deviations_nosso.append(deviation_nosso)
        
                i += 1
            print("", file=f)
            print("", file=f)
            print("Tempos de execucao: ", file=f)
            print(times, file=f)
            print("Media de erros comparado com exato networkx: ", file=f)
            print(errors_networkx, file=f)
            print("Media de erros comparado com exato nosso: ", file=f)
            print(errors_nosso, file=f)
            print("Desvio padrao comparado com exato networkx: ", file=f)
            print(deviations_networkx, file=f)
            print("Desvio padrao comparado com exato nosso: ", file=f)
            print(deviations_nosso, file=f)
        
            i = 0
    f.close
    del G
###########################################################################################

###########################################################################################
if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Use: python3.7 ./test_clustering <path_to_file> <out_file> <int: directed>")

    main(sys.argv[1], sys.argv[2], sys.argv[3])
###########################################################################################