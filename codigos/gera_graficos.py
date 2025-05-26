import matplotlib.pyplot as plt
import statistics

# Data
exact_nx_time = 0.015625
exact_author_time = 0.015625
approx_times = [0.125, 0.109375, 0.125, 0.109375, 0.125, 0.125, 0.109375, 0.109375, 0.125, 0.140625]

errors_vs_nx = [
    0.03031540450593572, 0.030055917244290808, 0.027995531976114492,
    0.02933074523038805, 0.032068833812642826, 0.028542955974642605,
    0.029454492258303606, 0.029255868993005155, 0.029311283397670137,
    0.03009880675199087
]

errors_vs_author = [
    0.030485436893203866, 0.029902912621359214, 0.027864077669902905,
    0.02902912621359222, 0.03194174757281551, 0.02834951456310678,
    0.029223300970873802, 0.02912621359223299, 0.02932038834951456,
    0.029902912621359228
]

std_vs_nx = [
    0.023064611643170755, 0.0233952293211972, 0.022107064242419098,
    0.023077601230559627, 0.024239075999188057, 0.023751548512240515,
    0.023462235050159378, 0.02350034875514533, 0.0238090523417482,
    0.023938395611806763
]

std_vs_author = [
    0.023530482557016896, 0.023786882325749773, 0.022656035120329356,
    0.023543184359296535, 0.024723670222904247, 0.02423543581141196,
    0.023896447893233176, 0.023942669534941445, 0.024234299819504604,
    0.024350798773890944
]

runs = list(range(1, 11))

# --- Figure 1: Average execution time per algorithm ---
plt.figure()
algo_names = ['Exact (NetworkX)', 'Exact (Author)', 'Approx (Mean)']
times = [exact_nx_time, exact_author_time, statistics.mean(approx_times)]
plt.bar(algo_names, times)
plt.ylabel('Execution Time (s)')
plt.title('Average Execution Time by Algorithm')
plt.tight_layout()
plt.show()

# --- Figure 2: Execution time of approximate algorithm per run ---
plt.figure()
plt.plot(runs, approx_times, marker='o')
plt.xlabel('Run')
plt.ylabel('Execution Time (s)')
plt.title('Approximate Algorithm Execution Time per Run')
plt.tight_layout()
plt.show()

# --- Figure 3: Mean error per run ---
plt.figure()
plt.plot(runs, errors_vs_nx, marker='o', label='Error vs NetworkX')
plt.plot(runs, errors_vs_author, marker='s', label='Error vs Author Exact')
plt.xlabel('Run')
plt.ylabel('Mean Absolute Error')
plt.title('Mean Clustering Error per Run')
plt.legend()
plt.tight_layout()
plt.show()

# --- Figure 4: Standard deviation of error per run ---
plt.figure()
plt.plot(runs, std_vs_nx, marker='o', label='Std Dev vs NetworkX')
plt.plot(runs, std_vs_author, marker='s', label='Std Dev vs Author Exact')
plt.xlabel('Run')
plt.ylabel('Standard Deviation')
plt.title('Error Standard Deviation per Run')
plt.legend()
plt.tight_layout()
plt.show()

# --- Figure 5: Mean error per run with reference line 0.04 ---
plt.figure()
plt.plot(runs, errors_vs_nx, marker='o', label='Error vs NetworkX')
plt.plot(runs, errors_vs_author, marker='s', label='Error vs Author Exact')
plt.hlines(0.04, runs[0], runs[-1], linestyles='--', label='Reference 0.04')
plt.xlabel('Run')
plt.ylabel('Mean Absolute Error')
plt.title('Mean Clustering Error per Run (with 0.04 Reference)')
plt.legend()
plt.tight_layout()
plt.show()

# --- Figure 6: Boxplot of approximate execution times ---
plt.figure()
plt.boxplot(approx_times, vert=True, labels=['Approx Alg'])
plt.ylabel('Execution Time (s)')
plt.title('Distribution of Approximate Algorithm Execution Time')
plt.tight_layout()
plt.show()

# --- Figure 7: Histogram of mean errors vs NetworkX ---
plt.figure()
plt.hist(errors_vs_nx, bins=5, edgecolor='black')
plt.xlabel('Mean Absolute Error')
plt.ylabel('Frequency')
plt.title('Histogram of Mean Errors (Approx vs NetworkX)')
plt.axvline(0.04, linestyle='--', label='0.04 Reference')
plt.legend()
plt.tight_layout()
plt.show()

# --- Figure 8: Error vs Execution Time scatter plot ---
mean_errors_vs_nx = errors_vs_nx  # alias for clarity
plt.figure()
plt.scatter(approx_times, mean_errors_vs_nx)
plt.xlabel('Execution Time (s)')
plt.ylabel('Mean Absolute Error vs NetworkX')
plt.title('Trade-off: Error vs Execution Time per Run')
plt.axhline(0.04, linestyle='--', label='0.04 Reference')
plt.legend()
plt.tight_layout()
plt.show()