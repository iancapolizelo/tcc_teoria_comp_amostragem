import matplotlib.pyplot as plt

# Definição dos epsilons usados em todos os grafos
epsilons = [0.04, 0.06, 0.08, 0.10]

# -------------------------------------------------------------------
# 1) BIO_CE_GN – Dados

# Tempos de execução (exato NetworkX, exato Nosso, aproximado BIO_CE_GN)
tempo_bio_nx         = [1.7779929339999998] * len(epsilons)
tempo_bio_nosso      = [39.028352913]       * len(epsilons)
tempo_bio_aproximado = [39.5658, 18.8698, 10.6040,  6.7647]

# Coeficientes médios (exato NetworkX, exato Nosso, aproximado BIO_CE_GN)
coef_bio_nx         = [0.19516173753689398] * len(epsilons)
coef_bio_nosso      = [0.18363963963963995] * len(epsilons)
coef_bio_aproximado = [0.1831303, 0.1866339, 0.1831950, 0.1789785]

# Erros médios (aproximado vs exato NetworkX, aproximado vs exato Nosso)
erro_bio_nx    = [0.03475, 0.05071, 0.06674, 0.08030]
erro_bio_nosso = [0.03436, 0.05055, 0.06640, 0.08026]

# Desvios padrão médios (aproximado vs exato NetworkX, aproximado vs exato Nosso)
dp_bio_nx    = [0.11580, 0.16139, 0.20988, 0.30493]
dp_bio_nosso = [0.11582, 0.16158, 0.20996, 0.30496]

# -------------------------------------------------------------------
# 2) ECON – Dados

# Tempos de execução (exato NetworkX, exato Nosso, aproximado ECON)
tempo_econ_nx         = [93.799679063]    * len(epsilons)
tempo_econ_nosso      = [4960.77196532]   * len(epsilons)
tempo_econ_aproximado = [1060.7246, 473.3427, 266.2181, 168.8927]

# Coeficientes médios (exato NetworkX, exato Nosso, aproximado ECON)
coef_econ_nx         = [0.49637472151094525] * len(epsilons)
coef_econ_nosso      = [0.5106337579617815]   * len(epsilons)
coef_econ_aproximado = [0.5093815, 0.5111392, 0.5098729, 0.5060557]

# Erros médios (aproximado vs exato NetworkX, aproximado vs exato Nosso)
erro_econ_nx    = [0.01836, 0.02481, 0.03056, 0.03703]
erro_econ_nosso = [0.01449, 0.02132, 0.02832, 0.03642]

# Desvios padrão médios (aproximado vs exato NetworkX, aproximado vs exato Nosso)
dp_econ_nx    = [0.02324, 0.03475, 0.04221, 0.05546]
dp_econ_nosso = [0.02103, 0.03129, 0.04055, 0.05384]

# -------------------------------------------------------------------
# 3) CAIDA – Dados

# Tempos de execução (exato NetworkX, exato Nosso, aproximado CAIDA)
tempo_caida_nx         = [9.4877]    * len(epsilons)
tempo_caida_nosso      = [136.5918]  * len(epsilons)
tempo_caida_aproximado = [20.9661, 9.3272, 5.4710, 3.7462]

# Coeficientes médios (exato NetworkX, exato Nosso, aproximado CAIDA)
coef_caida_nx         = [0.2020549] * len(epsilons)
coef_caida_nosso      = [0.1582255] * len(epsilons)
coef_caida_aproximado = [0.1585978, 0.1605787, 0.1556172, 0.1599613]

# Erros médios (aproximado vs exato NetworkX, aproximado vs exato Nosso)
erro_caida_nx    = [0.2132494, 0.2561518, 0.2711537, 0.2877582]
erro_caida_nosso = [0.2132640, 0.2561877, 0.2711988, 0.2878033]

# Desvios padrão médios (aproximado vs exato NetworkX, aproximado vs exato Nosso)
dp_caida_nx    = [0.6726889, 1.0356586, 1.3545228, 1.7805094]
dp_caida_nosso = [0.6726821, 1.0356499, 1.3545159, 1.7805041]

# -------------------------------------------------------------------
# 1) Gráficos de tempo – separados por grafo

# BIO_CE_GN – Tempo de Execução
plt.figure(figsize=(8, 5))
plt.plot(epsilons, tempo_bio_nx,      marker='o', color='orange', label='BIO_CE_GN NX (Exato)')
plt.plot(epsilons, tempo_bio_nosso,   marker='o', color='green',  label='BIO_CE_GN Nosso (Exato)')
plt.plot(epsilons, tempo_bio_aproximado, marker='o', color='blue',   label='BIO_CE_GN Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Tempo de Execução (s)')
plt.title('BIO_CE_GN – Comparação de Tempos de Execução')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ECON – Tempo de Execução
plt.figure(figsize=(8, 5))
plt.plot(epsilons, tempo_econ_nx,      marker='o', color='orange', label='ECON NX (Exato)')
plt.plot(epsilons, tempo_econ_nosso,   marker='o', color='green',  label='ECON Nosso (Exato)')
plt.plot(epsilons, tempo_econ_aproximado, marker='o', color='purple', label='ECON Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Tempo de Execução (s)')
plt.title('ECON – Comparação de Tempos de Execução')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# CAIDA – Tempo de Execução
plt.figure(figsize=(8, 5))
plt.plot(epsilons, tempo_caida_nx,      marker='o', color='orange', label='CAIDA NX (Exato)')
plt.plot(epsilons, tempo_caida_nosso,   marker='o', color='green',  label='CAIDA Nosso (Exato)')
plt.plot(epsilons, tempo_caida_aproximado, marker='o', color='red',    label='CAIDA Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Tempo de Execução (s)')
plt.title('CAIDA – Comparação de Tempos de Execução')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 2) Gráficos de coeficiente – separados por grafo

# BIO_CE_GN – Coeficiente Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, coef_bio_nx,      marker='o', color='orange', label='BIO_CE_GN NX (Exato)')
plt.plot(epsilons, coef_bio_nosso,   marker='o', color='green',  label='BIO_CE_GN Nosso (Exato)')
plt.plot(epsilons, coef_bio_aproximado, marker='o', color='blue',   label='BIO_CE_GN Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Coeficiente de Clustering Local Médio')
plt.title('BIO_CE_GN – Comparação dos Coeficientes Médios')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ECON – Coeficiente Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, coef_econ_nx,      marker='o', color='orange', label='ECON NX (Exato)')
plt.plot(epsilons, coef_econ_nosso,   marker='o', color='green',  label='ECON Nosso (Exato)')
plt.plot(epsilons, coef_econ_aproximado, marker='o', color='purple', label='ECON Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Coeficiente de Clustering Local Médio')
plt.title('ECON – Comparação dos Coeficientes Médios')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# CAIDA – Coeficiente Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, coef_caida_nx,      marker='o', color='orange', label='CAIDA NX (Exato)')
plt.plot(epsilons, coef_caida_nosso,   marker='o', color='green',  label='CAIDA Nosso (Exato)')
plt.plot(epsilons, coef_caida_aproximado, marker='o', color='red',    label='CAIDA Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Coeficiente de Clustering Local Médio')
plt.title('CAIDA – Comparação dos Coeficientes Médios')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 3) Gráficos de erro médio – separados por grafo

# BIO_CE_GN – Erro Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, erro_bio_nx,    marker='o', color='orange', label='BIO_CE_GN Erro (vs NX)')
plt.plot(epsilons, erro_bio_nosso, marker='o', color='green',  label='BIO_CE_GN Erro (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Erro Médio')
plt.title('BIO_CE_GN – Erro Médio vs Epsilon')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ECON – Erro Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, erro_econ_nx,    marker='o', color='orange', label='ECON Erro (vs NX)')
plt.plot(epsilons, erro_econ_nosso, marker='o', color='green',  label='ECON Erro (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Erro Médio')
plt.title('ECON – Erro Médio vs Epsilon')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# CAIDA – Erro Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, erro_caida_nx,    marker='o', color='orange', label='CAIDA Erro (vs NX)')
plt.plot(epsilons, erro_caida_nosso, marker='o', color='green',  label='CAIDA Erro (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Erro Médio')
plt.title('CAIDA – Erro Médio vs Epsilon')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 4) Gráficos de desvio padrão médio – separados por grafo

# BIO_CE_GN – Desvio Padrão Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, dp_bio_nx,    marker='o', color='orange', label='BIO_CE_GN DP (vs NX)')
plt.plot(epsilons, dp_bio_nosso, marker='o', color='green',  label='BIO_CE_GN DP (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Desvio Padrão Médio')
plt.title('BIO_CE_GN – Desvio Padrão Médio vs Epsilon')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ECON – Desvio Padrão Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, dp_econ_nx,    marker='o', color='orange', label='ECON DP (vs NX)')
plt.plot(epsilons, dp_econ_nosso, marker='o', color='green',  label='ECON DP (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Desvio Padrão Médio')
plt.title('ECON – Desvio Padrão Médio vs Epsilon')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# CAIDA – Desvio Padrão Médio
plt.figure(figsize=(8, 5))
plt.plot(epsilons, dp_caida_nx,    marker='o', color='orange', label='CAIDA DP (vs NX)')
plt.plot(epsilons, dp_caida_nosso, marker='o', color='green',  label='CAIDA DP (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Desvio Padrão Médio')
plt.title('CAIDA – Desvio Padrão Médio vs Epsilon')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
