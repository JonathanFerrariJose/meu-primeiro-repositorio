import numpy as np

notas = np.array([
    [8.5, 9.0, 7.5],
    [6.0, 7.5, 5.0],
    [9.5, 8.0, 9.0],
    [5.0, 6.0, 4.5]
])
min_vals = notas.min(axis=0)
max_vals = notas.max(axis=0)
min_max_norm = (notas - min_vals) / (max_vals - min_vals)

mean_vals = notas.mean(axis=0)
std_vals = notas.std(axis=0)
z_score_norm = (notas - mean_vals) / std_vals

print("Min-Max:\n", min_max_norm)
print("Z-score:\n", z_score_norm)