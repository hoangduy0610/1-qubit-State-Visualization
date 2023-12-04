from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_quantum_states(quantum_states):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for state in quantum_states:
        if len(state) == 2:
            state = np.append(state, 0)
        plot_bloch_vector(state, ax=ax)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere')

    plt.show()

def main():
    quantum_states = [
        np.array([1, 0]),
        np.array([0, 1])
    ]

    plot_quantum_states(quantum_states)

if __name__ == "__main__":
    main()
