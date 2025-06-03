import matplotlib.pyplot as plt

# Dados fornecidos
epsilons = [0.04, 0.06, 0.08, 0.10]

# ----------------------------
# BIO_CE_GN – Tempos de execução
tempo_bio_nx = [1.7779929339999998] * len(epsilons)
tempo_bio_nosso = [39.028352913] * len(epsilons)
tempo_bio_aproximado = [39.5658, 18.8698, 10.6040, 6.7647]

# ECON – Tempos de execução
tempo_econ_nx = [93.799679063] * len(epsilons)
tempo_econ_nosso = [4960.77196532] * len(epsilons)
tempo_econ_aproximado = [1060.7246, 473.3427, 266.2181, 168.8927]

# ----------------------------
# BIO_CE_GN – Coeficientes médios
coef_bio_nx = [0.19516173753689398] * len(epsilons)
coef_bio_nosso = [0.18363963963963995] * len(epsilons)
coef_bio_aproximado = [0.1831303, 0.1866339, 0.1831950, 0.1789785]

# ECON – Coeficientes médios
coef_econ_nx = [0.49637472151094525] * len(epsilons)
coef_econ_nosso = [0.5106337579617815] * len(epsilons)
coef_econ_aproximado = [0.5093815, 0.5111392, 0.5098729, 0.5060557]

# ----------------------------
# BIO_CE_GN – Erros médios
erro_bio_nx = [0.03475, 0.05071, 0.06674, 0.08030]
erro_bio_nosso = [0.03436, 0.05055, 0.06640, 0.08026]

# ECON – Erros médios
erro_econ_nx = [0.01836, 0.02481, 0.03056, 0.03703]
erro_econ_nosso = [0.01449, 0.02132, 0.02832, 0.03642]

# ----------------------------
# BIO_CE_GN – Desvios padrão médios
dp_bio_nx = [0.11580, 0.16139, 0.20988, 0.30493]
dp_bio_nosso = [0.11582, 0.16158, 0.20996, 0.30496]

# ECON – Desvios padrão médios
dp_econ_nx = [0.02324, 0.03475, 0.04221, 0.05546]
dp_econ_nosso = [0.02103, 0.03129, 0.04055, 0.05384]

# -------------------------------------------------------------------
# 1) Gráfico de comparação de tempos - BIO_CE_GN
plt.figure(figsize=(8, 5))
plt.plot(epsilons, tempo_bio_nx, marker='o', color='orange', label='BIO_CE_GN NX (Exato)')
plt.plot(epsilons, tempo_bio_nosso, marker='o', color='green', label='BIO_CE_GN Nosso (Exato)')
plt.plot(epsilons, tempo_bio_aproximado, marker='o', color='blue', label='BIO_CE_GN Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Tempo de Execução (s)')
plt.title('BIO_CE_GN – Comparação de Tempos de Execução')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2) Gráfico de comparação de tempos - ECON
plt.figure(figsize=(8, 5))
plt.plot(epsilons, tempo_econ_nx, marker='o', color='orange', label='ECON NX (Exato)')
plt.plot(epsilons, tempo_econ_nosso, marker='o', color='green', label='ECON Nosso (Exato)')
plt.plot(epsilons, tempo_econ_aproximado, marker='o', color='purple', label='ECON Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Tempo de Execução (s)')
plt.title('ECON – Comparação de Tempos de Execução')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 3) Gráfico de comparação de coeficientes - BIO_CE_GN
plt.figure(figsize=(8, 5))
plt.plot(epsilons, coef_bio_nx, marker='o', color='orange', label='BIO_CE_GN NX (Exato)')
plt.plot(epsilons, coef_bio_nosso, marker='o', color='green', label='BIO_CE_GN Nosso (Exato)')
plt.plot(epsilons, coef_bio_aproximado, marker='o', color='blue', label='BIO_CE_GN Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Coeficiente de Clustering Local Médio')
plt.title('BIO_CE_GN – Comparação dos Coeficientes Médios')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 4) Gráfico de comparação de coeficientes - ECON
plt.figure(figsize=(8, 5))
plt.plot(epsilons, coef_econ_nx, marker='o', color='orange', label='ECON NX (Exato)')
plt.plot(epsilons, coef_econ_nosso, marker='o', color='green', label='ECON Nosso (Exato)')
plt.plot(epsilons, coef_econ_aproximado, marker='o', color='purple', label='ECON Aproximado')
plt.xlabel('Epsilon')
plt.ylabel('Coeficiente de Clustering Local Médio')
plt.title('ECON – Comparação dos Coeficientes Médios')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 5) Erro Médio vs Epsilon (BIO_CE_GN + ECON)
plt.figure(figsize=(8, 5))
plt.plot(epsilons, erro_bio_nx, marker='o', color='orange', linestyle='-', label='BIO_CE_GN Erro (vs NX)')
plt.plot(epsilons, erro_bio_nosso, marker='o', color='green', linestyle='-', label='BIO_CE_GN Erro (vs Nosso)')
plt.plot(epsilons, erro_econ_nx, marker='s', color='orange', linestyle='--', label='ECON Erro (vs NX)')
plt.plot(epsilons, erro_econ_nosso, marker='s', color='green', linestyle='--', label='ECON Erro (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Erro Médio')
plt.title('Erro Médio vs Epsilon (BIO_CE_GN + ECON)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 6) Desvio Padrão Médio vs Epsilon (BIO_CE_GN + ECON)
plt.figure(figsize=(8, 5))
plt.plot(epsilons, dp_bio_nx, marker='o', color='orange', linestyle='-', label='BIO_CE_GN DP (vs NX)')
plt.plot(epsilons, dp_bio_nosso, marker='o', color='green', linestyle='-', label='BIO_CE_GN DP (vs Nosso)')
plt.plot(epsilons, dp_econ_nx, marker='s', color='orange', linestyle='--', label='ECON DP (vs NX)')
plt.plot(epsilons, dp_econ_nosso, marker='s', color='green', linestyle='--', label='ECON DP (vs Nosso)')
plt.xlabel('Epsilon')
plt.ylabel('Desvio Padrão Médio')
plt.title('Desvio Padrão Médio vs Epsilon (BIO_CE_GN + ECON)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
