import numpy as np
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_states_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        quantum_states = [complex(line.strip('()\n')) for line in lines]
    return quantum_states

def calculate_theta_phi(state):
    theta = 2 * np.arccos(np.abs(state.real))
    phi = np.angle(state) if theta != 0 else 0
    return theta, phi

def plot_quantum_states(quantum_states):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for state in quantum_states:
        theta, phi = calculate_theta_phi(state)

        # Hiển thị đầu mũi tên
        bloch_vector = [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]
        plot_bloch_vector(bloch_vector, ax=ax)

        # # Hiển thị văn bản mô tả trạng thái
        # text_position = np.array([1.2 * np.sin(theta) * np.cos(phi), 1.2 * np.sin(theta) * np.sin(phi), 1.2 * np.cos(theta)])
        # ax.text(text_position[0], text_position[1], text_position[2], f'State: {state}', color='blue')

        # # Hiển thị đường cung và số đo góc
        # arc_radius = 1.2
        # arc_points = np.array([arc_radius * np.sin(t), arc_radius * np.cos(t), 0]) for t in np.linspace(0, phi, 100)])
        # ax.plot(arc_points[:, 0], arc_points[:, 1], arc_points[:, 2], linestyle='dashed', color='black')
        # ax.text(0.8 * np.sin(phi / 2), 0.8 * np.cos(phi / 2), 0, f'{phi/np.pi:.2f}$\\pi$', color='red')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere', pad=50)

    plt.show()

def main():
    file_path = 'complex.txt'  # Đặt tên file txt của bạn ở đây
    quantum_states = read_states_from_file(file_path)
    plot_quantum_states(quantum_states)

if __name__ == "__main__":
    main()
