from matplotlib import pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

def calculate_rotation_angles(initial_state, target_state):
    # Tính toán góc xoay cho cổng rx
    rx_angle = np.arctan2(np.sqrt(initial_state[1]**2 + target_state[1]**2), target_state[0] - initial_state[0])

    # Tính toán góc xoay cho cổng ry
    ry_angle = np.arctan2(target_state[1], target_state[0])

    # Tính toán góc xoay cho cổng rz
    rz_angle = np.angle(target_state[1] / np.sin(ry_angle)) if np.sin(ry_angle) != 0 else 0

    return rx_angle, ry_angle, rz_angle

def Visualization(initial_state, target_state):
    # initial_state = np.array([1, 0])
    # target_state = np.array([0, 1])
    # Tính toán góc xoay
    rx_angle, ry_angle, rz_angle = calculate_rotation_angles(initial_state, target_state)

    # Tạo mạch lượng tử và áp dụng cổng xoay
    qc = QuantumCircuit(1)
    qc.rx(rx_angle, 0)
    qc.ry(ry_angle, 0)
    qc.rz(rz_angle, 0)

    # Hiển thị mạch lượng tử và quá trình chuyển động
    qc.draw('mpl')
    plt.show()
    # visualize_transition(qc, trace=True, saveas="rotation_gates.gif", fpg=30, spg=5)
    visualize_transition(qc, trace=True, fpg=30, spg=5)
    