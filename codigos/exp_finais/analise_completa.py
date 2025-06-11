import re
import json
import matplotlib.pyplot as plt
import numpy as np

# Função para parsear arquivo de resultados de um grafo
def parse_results(filepath):
    with open(filepath, 'r') as f:
        text = f.read()

    # Extrair valores exatos
    exact_nx_time = float(re.search(r"Total de tempo de execucao do algoritmo exato .*?([\d\.]+)", text).group(1))
    exact_nx_coef = float(re.search(r"Media dos coeficientes de clustering local do algoritmo exato .*?=\s*([\d\.]+)", text).group(1))
    exact_nosso_time = float(re.search(r"Total de tempo de execucao do algoritmo exato \(autoral\): ([\d\.]+)", text).group(1))
    exact_nosso_coef = float(re.search(r"Media dos coeficientes de clustering local do algoritmo exato .*?\(autoral\)\s*=\s*([\d\.]+)", text).group(1))

    # Dicionário para armazenar dados por epsilon
    data = {
        'exact_nx_time': exact_nx_time,
        'exact_nx_coef': exact_nx_coef,
        'exact_nosso_time': exact_nosso_time,
        'exact_nosso_coef': exact_nosso_coef,
        'epsilons': {}
    }

    # Regex para cada bloco de 10 iterações por epsilon
    iter_block_pattern = re.compile(
        r"Iteracao: \d+\s*epsilon:\s*([\d\.]+).*?Numero de amostras eh r = (\d+).*?"
        r"Total de tempo de execucao do algoritmo de aproximacao: ([\d\.]+).*?"
        r"Quantidade de Zeros = (\d+).*?"
        r"Media dos coeficientes de clustering local do algoritmo aproximado = ([\d\.]+)",
        re.S
    )

    # Encontrar todas as ocorrências de iteração
    matches = iter_block_pattern.findall(text)

    # Agrupar por epsilon
    for eps, r_val, time_val, zeros_val, coef_val in matches:
        eps = float(eps)
        if eps not in data['epsilons']:
            data['epsilons'][eps] = {'r': [], 'time': [], 'zeros': [], 'coef': []}
        data['epsilons'][eps]['r'].append(int(r_val))
        data['epsilons'][eps]['time'].append(float(time_val))
        data['epsilons'][eps]['zeros'].append(int(zeros_val))
        data['epsilons'][eps]['coef'].append(float(coef_val))

    # Extrair listas de erros e desvios padrão por epsilon (na ordem de aparecimento)
    array_pattern = re.compile(
        r"Tempos de execucao:\s*\n(\[.*?\])\s*"
        r"Media de erros comparado com exato networkx:\s*\n(\[.*?\])\s*"
        r"Media de erros comparado com exato nosso:\s*\n(\[.*?\])\s*"
        r"Desvio padrao comparado com exato networkx:\s*\n(\[.*?\])\s*"
        r"Desvio padrao comparado com exato nosso:\s*\n(\[.*?\])",
        re.S
    )

    arrays = array_pattern.findall(text)
    epsilons_sorted = sorted(data['epsilons'].keys())
    for i, eps in enumerate(epsilons_sorted):
        times_list      = json.loads(arrays[i][0])
        err_nx_list     = json.loads(arrays[i][1])
        err_nosso_list  = json.loads(arrays[i][2])
        dp_nx_list      = json.loads(arrays[i][3])
        dp_nosso_list   = json.loads(arrays[i][4])

        data['epsilons'][eps]['times_list']     = times_list
        data['epsilons'][eps]['err_nx_list']    = err_nx_list
        data['epsilons'][eps]['err_nosso_list'] = err_nosso_list
        data['epsilons'][eps]['dp_nx_list']     = dp_nx_list
        data['epsilons'][eps]['dp_nosso_list']  = dp_nosso_list

    return data

# ---- Parsear arquivos ----
bioCE  = parse_results("testeNOVO2_bioCE.txt")
econ   = parse_results("tesetNOVO_econ.txt")
caida  = parse_results("testeCAIDA.txt")
nasa  = parse_results("testeNOVO_scnasa.txt")
shipsec5  = parse_results("testeNOVO_shipsec5.txt")

# Epsilons (mesmos para todos)
epsilons = sorted(bioCE['epsilons'].keys())

# 1) Boxplots dos coeficientes aproximados por ε para cada grafo
for nome, dataset in [("BIO_CE_GN", bioCE), ("ECON", econ), ("CAIDA", caida), ("NASA", nasa), ("SHIPSEC5", shipsec5)]:
    dados_coefs = [dataset['epsilons'][eps]['coef'] for eps in epsilons]
    plt.figure(figsize=(8, 5))
    plt.boxplot(dados_coefs, labels=[f"ε={eps}" for eps in epsilons])
    plt.xlabel("Epsilon")
    plt.ylabel("Coeficiente de Clustering Local")
    plt.title(f"{nome} – Distribuição dos Coeficientes Aproximados por ε")
    plt.grid(linestyle=":", alpha=0.5)
    plt.tight_layout()
    plt.show()

# 2) Boxplots dos erros absolutos por ε para cada grafo (em relação ao exato NetworkX)
for nome, dataset in [("BIO_CE_GN", bioCE), ("ECON", econ), ("CAIDA", caida), ("NASA", nasa), ("SHIPSEC5", shipsec5)]:
    dados_erros = [dataset['epsilons'][eps]['err_nx_list'] for eps in epsilons]
    plt.figure(figsize=(8, 5))
    plt.boxplot(dados_erros, labels=[f"ε={eps}" for eps in epsilons])
    plt.xlabel("Epsilon")
    plt.ylabel("Erro Absoluto vs NetworkX")
    plt.title(f"{nome} – Distribuição dos Erros vs NetworkX por ε")
    plt.grid(linestyle=":", alpha=0.5)
    plt.tight_layout()
    plt.show()

# 3) Scatter plot – Erro vs Tempo para cada grafo e ε
plt.figure(figsize=(8, 5))
for nome, dataset, cor in [("BIO_CE_GN", bioCE, 'blue'), ("ECON", econ, 'purple'), ("CAIDA", caida, 'red'), ("NASA", nasa, 'green'), ("SHIPSEC5", shipsec5, 'orange')]:
    tempos = [np.mean(dataset['epsilons'][eps]['time']) for eps in epsilons]
    erros  = [np.mean(dataset['epsilons'][eps]['err_nx_list']) for eps in epsilons]
    plt.scatter(tempos, erros, color=cor, label=nome)
    for i, eps in enumerate(epsilons):
        plt.annotate(f"ε={eps}", (tempos[i], erros[i]), color=cor)

plt.xlabel("Tempo Médio de Execução (s)")
plt.ylabel("Erro Médio vs NetworkX")
plt.title("Trade‐Off: Erro vs Tempo para cada Grafo e ε")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

# 4) Speedup dos aproximados em relação ao exato NetworkX
plt.figure(figsize=(8, 5))
for nome, dataset, cor in [("BIO_CE_GN", bioCE, 'blue'), ("ECON", econ, 'purple'), ("CAIDA", caida, 'red'), ("NASA", nasa, 'green'), ("SHIPSEC5", shipsec5, 'orange')]:
    speedup = [dataset['exact_nx_time'] / np.mean(dataset['epsilons'][eps]['time']) for eps in epsilons]
    plt.plot(epsilons, speedup, marker='o', color=cor, label=nome)

plt.xlabel("Epsilon")
plt.ylabel("Speedup (Exato NX / Aproximado)")
plt.title("Speedup dos Aproximados em Relação ao Exato NetworkX")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

# 5) Erro relativo (%) vs ε para cada grafo
plt.figure(figsize=(8, 5))
for nome, dataset, cor in [("BIO_CE_GN", bioCE, 'blue'), ("ECON", econ, 'purple'), ("CAIDA", caida, 'red'), ("NASA", nasa, 'green'), ("SHIPSEC5", shipsec5, 'orange')]:
    erro_relativo = [
        abs(np.mean(dataset['epsilons'][eps]['coef']) - dataset['exact_nx_coef']) / dataset['exact_nx_coef'] * 100 
        for eps in epsilons
    ]
    plt.plot(epsilons, erro_relativo, marker='o', color=cor, label=nome)

plt.xlabel("Epsilon")
plt.ylabel("Erro Relativo (%) vs NetworkX")
plt.title("Erro Relativo (%) dos Coeficientes Aproximados")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

# 6) Heatmap do Erro Médio vs NetworkX (matriz: grafo × ε)
matriz_erro = np.array([
    [np.mean(bioCE['epsilons'][eps]['err_nx_list']) for eps in epsilons],
    [np.mean(econ['epsilons'][eps]['err_nx_list']) for eps in epsilons],
    [np.mean(caida['epsilons'][eps]['err_nx_list']) for eps in epsilons]
])

plt.figure(figsize=(6, 4))
plt.imshow(matriz_erro, cmap='viridis', aspect='auto')
plt.colorbar(label="Erro Médio vs NX")
plt.xticks(range(len(epsilons)), [str(e) for e in epsilons])
plt.yticks([0, 1, 2], ["BIO_CE_GN", "ECON", "CAIDA", "NASA", "SHIPSEC5"])
plt.xlabel("Epsilon")
plt.title("Heatmap do Erro Médio vs NetworkX")
plt.tight_layout()
plt.show()

# 7) Spaghetti plot – Coeficiente por Iteração vs ε para cada grafo
for nome, dataset, cor in [("BIO_CE_GN", bioCE, 'blue'), ("ECON", econ, 'purple'), ("CAIDA", caida, 'red'), ("NASA", nasa, 'green'), ("SHIPSEC5", shipsec5, 'orange')]:
    plt.figure(figsize=(8, 5))
    coef_matrix = np.array([dataset['epsilons'][eps]['coef'] for eps in epsilons]).T
    for i in range(coef_matrix.shape[0]):
        plt.plot(epsilons, coef_matrix[i], color=cor, alpha=0.5)
    plt.xlabel("Epsilon")
    plt.ylabel("Coeficiente de Clustering Local")
    plt.title(f"{nome} – Coeficiente Aproximado por Iteração")
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.tight_layout()
    plt.show()

# 8) Heatmap de Quantidade de Zeros (iteração × ε) – apenas CAIDA
zeros_caida = np.array([caida['epsilons'][eps]['zeros'] for eps in epsilons])

plt.figure(figsize=(6, 4))
plt.imshow(zeros_caida, cmap='magma', aspect='auto')
plt.colorbar(label="Qtd. de Zeros")
plt.xticks(range(10), [f"i={i}" for i in range(10)], rotation=45)
plt.yticks(range(len(epsilons)), [f"ε={eps}" for eps in epsilons])
plt.xlabel("Iteração")
plt.ylabel("Epsilon")
plt.title("CAIDA – Heatmap de Quantidade de Zeros")
plt.tight_layout()
plt.show()

# 9) Boxplot dos coeficientes aproximados agrupados por grafo (todos os epsilons)
coef_bio_all   = np.concatenate([bioCE['epsilons'][eps]['coef'] for eps in epsilons])
coef_econ_all  = np.concatenate([econ['epsilons'][eps]['coef'] for eps in epsilons])
coef_caida_all = np.concatenate([caida['epsilons'][eps]['coef'] for eps in epsilons])

plt.figure(figsize=(6, 4))
plt.boxplot([coef_bio_all, coef_econ_all, coef_caida_all], labels=["BIO_CE_GN","ECON","CAIDA", "NASA", "SHIPSEC5"])
plt.ylabel("Coeficiente Aproximado")
plt.title("Comparação das Distribuições de Coeficientes Aproximados")
plt.grid(linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

# 10) Scatter plot – Tempo vs Quantidade de Zeros (CAIDA)
tempos_caida_all = np.concatenate([caida['epsilons'][eps]['time'] for eps in epsilons])
zeros_caida_all  = np.concatenate([caida['epsilons'][eps]['zeros'] for eps in epsilons])

plt.figure(figsize=(6, 4))
plt.scatter(zeros_caida_all, tempos_caida_all, alpha=0.7, color='red')
plt.xlabel("Quantidade de Zeros")
plt.ylabel("Tempo de Execução (s)")
plt.title("CAIDA – Tempo vs Qtd. de Zeros (todas as rodadas)")
plt.grid(linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

# 11) Plot do número de amostras r vs ε (CAIDA)
plt.figure(figsize=(6, 4))
for eps in epsilons:
    plt.scatter([eps]*10, caida['epsilons'][eps]['r'], label=f"ε={eps}")
plt.xlabel("Epsilon")
plt.ylabel("Número de Amostras r")
plt.title("CAIDA – Distribuição de r por Epsilon (10 rodadas)")
plt.legend()
plt.grid(linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()
