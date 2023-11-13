import numpy as np
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_states_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        quantum_states = [np.array([float(x) for x in line.split()]) for line in lines]
    return quantum_states

def calculate_theta_phi(state):
    # Tính toán giá trị theta và phi từ trạng thái
    theta = 2 * np.arccos(np.abs(state[0]))
    phi = np.angle(state[1] / np.sin(theta / 2)) if theta != 0 else 0
    return theta, phi

def plot_quantum_states(quantum_states):
    fig = plt.figure()
    fig.canvas.manager.set_window_title('Test')
    ax = fig.add_subplot(111, projection='3d')

    for state in quantum_states:
        theta, phi = calculate_theta_phi(state)
        # plot_bloch_vector([np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)], ax=ax)

        # Hiển thị đầu mũi tên
        bloch_vector = [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]
        plot_bloch_vector(bloch_vector, ax=ax)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere', pad=50)

    plt.show()

def main():
    file_path = 'input.txt'  # Đặt tên file txt của bạn ở đây
    quantum_states = read_states_from_file(file_path)
    plot_quantum_states(quantum_states)

if __name__ == "__main__":
    main()
