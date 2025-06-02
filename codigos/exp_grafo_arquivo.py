import networkx as nx
import time
import os
import operator
import sys
from statistics import stdev 
from local_clustering_approximation import local_clustering_approximation, local_clustering_exato

###########################################################################################
def read_graph(file_path):
    """
    Lê .edges (u v [w]) ou Matrix Market (.mtx) e devolve um Graph/DiGraph.

    Parameters
    ----------
    file_path : str
        Caminho do arquivo.

    Returns
    -------
    G : nx.Graph
    """
    G = nx.Graph()
    ext = os.path.splitext(file_path)[1].lower()
    is_mtx = ext == ".mtx"

    with open(file_path, "r", encoding="utf-8") as f:
        size_line_skipped = False           # só para .mtx

        for line in f:
            # Comentários em qualquer formato começam com %
            if line.startswith("%"):
                continue

            # .mtx: a 1ª linha não comentada é "n m nnz" – descartamos
            if is_mtx and not size_line_skipped:
                size_line_skipped = True
                continue

            parts = line.split()
            if len(parts) < 2:
                continue                    # linha vazia ou mal-formada

            u, v = parts[0], parts[1]
            
            G.add_edge(u, v)

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

def media_networkx(G, C):
    """Calcula a média dos valores de um dicionário, considerando apenas os nós com grau maior que 1."""
    
    valores_validos = [c for n, c in C.items() if G.degree(n) > 1]
    media_correta = sum(valores_validos) / len(valores_validos)
    return(media_correta)

###########################################################################################
def main(in_file: str, out_file: str):

    G = read_graph(in_file)

    m = G.number_of_edges()
    max_degree = max(G.degree, key=operator.itemgetter(1))[1]
    universalConstant=0.5
    edges_list = list(G.edges())

    with open(out_file, 'w') as f:
        print("###########################################################################################", file=f)
        print("Nova rodada de testes: \n", file=f)
        print("O grafo tem {} vertices e {} arestas".format(G.number_of_nodes(), G.number_of_edges()), file=f)

        t1 = time.process_time()
        clustering_exato_networkx = nx.clustering(G)
        print("Total de tempo de execucao do algoritmo exato (lib networkx): " + str(time.process_time() - t1), file=f)
        #print("Exact coefficient clustering values: \n" + ', '.join('{:0.20f}'.format(pc_ord[i]) for i in pc_ord) + "\n", file=f)
        media_exato_networkx = media_networkx(G, clustering_exato_networkx)
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
                #parameters
                local_clustering = {}
                t_aprox = {}

                for v in G.nodes():
                    t_aprox[v] = 0
                    local_clustering[v] = 0

                t2 = time.process_time()
                pc_tilde = local_clustering_approximation(G, float(e), float(delta), float(p), f, max_degree, m, universalConstant, local_clustering, t_aprox, edges_list)
                t_medio = time.process_time() - t2
                print("Total de tempo de execucao do algoritmo de aproximacao: " + str(t_medio), file=f)
                times.append(t_medio)
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
    if len(sys.argv) != 3:
        sys.exit("Use: python exp_grafo_arquivo.py <path_to_file> <out_file>")

    main(sys.argv[1], sys.argv[2])
###########################################################################################