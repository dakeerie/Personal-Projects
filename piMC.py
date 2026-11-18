import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N):

    inside_circle = 0
    inner_x, inner_y = [], []
    outer_x, outer_y = [], []

    for n in range(N):
        x, y = 2*np.random.random() - 1, 2*np.random.random() - 1
        distance = np.sqrt(x**2 + y**2)

        if distance <= 1:
            inside_circle += 1
            inner_x.append(x)
            inner_y.append(y)

        else:
            outer_x.append(x)
            outer_y.append(y)


    pi_estimate = (inside_circle/N)*4

    plt.figure(figsize = [5, 5])
    plt.scatter(inner_x, inner_y, color = 'red', s = 1, label =  'Inside')
    plt.scatter(outer_x, outer_y, color = 'blue', s = 1, label = 'Outside')
    plt.xlabel('x', fontsize = 12)
    plt.ylabel('y', fontsize = 12)
    plt.tight_layout()
    plt.legend()
    plt.show()

    # print(x, y)
    return pi_estimate

pi_estimation = estimate_pi(10000)
print(f"Estimated value of Pi: {pi_estimation}")
