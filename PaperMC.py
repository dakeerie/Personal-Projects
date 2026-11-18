import numpy as np
import matplotlib.pyplot as ply

tasks = {'Method': (4, 6, 9), 'Results': (2, 3, 5), 'Background': (4, 6, 9), 'Intoduction': (1, 2, 3), 'Conclusion': ( 1, 2, 3), 'Abstract': (1, 1.5, 2)}

simulations = 10000
total_durations = np.zeros(simulations)

for task, (opt, likely, pess) in tasks.items():
    samples = np.random.triangular(opt, likely, pess, simulations)
    total_durations += samples

naive_estimate = sum(t[1] for t in tasks.values()) #i.e. sum of likely times not accounting for drift between tasks
p50 = np.percentile(total_durations, 50)
p85 = np.percentile(total_durations, 85)

print(f"Naive Estimate (Sum of most likely): {naive_estimate} hours")
print(f"50% Confidence (Median): {p50:.1f} hours")
print(f"85% Confidence (Safe Deadline): {p85:.1f} hours")