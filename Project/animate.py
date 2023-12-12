from matplotlib import pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from custom_packages.transition_visualization import visualize_transition
from plotter import calculate_phi_and_theta
from config import ANIMATE_FILE_NAME, FPG_ANIMATE, SAVE_ANIMATE_TO_FILE, SPG_ANIMATE

def Oxy(inp):
    return np.array([inp[0], inp[1]])
def Oyz(inp):
    return np.array([inp[1], inp[2]])
def Oxz(inp):
    return np.array([inp[0], inp[2]])

def angle(vector1, vector2):
    A = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    B = np.sqrt(vector1[0]**2 + vector1[1]**2) * np.sqrt(vector2[0]**2 + vector2[1]**2)

    if B == 0:
        return 0

    return np.arccos(A / B)

def calculate_rotation_angles(initial_state, target_state):
    # Tính toán góc xoay cho cổng rx
    rx_angle = angle(Oyz(initial_state), Oyz(target_state))

    # Tính toán góc xoay cho cổng ry
    ry_angle = angle(Oxz(initial_state), Oxz(target_state))

    # Tính toán góc xoay cho cổng rz
    rz_angle = angle(Oxy(initial_state), Oxy(target_state))

    return rx_angle, ry_angle, rz_angle

def visualization(i_s, t_s):
    theta, phi = calculate_phi_and_theta(i_s[0], i_s[1])
    init_vector_state = np.array([np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)])

    theta, phi = calculate_phi_and_theta(t_s[0], t_s[1])
    target_vector_state = np.array([np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)])
    # Tính toán góc xoay
    rx_angle, ry_angle, rz_angle = calculate_rotation_angles(init_vector_state, target_vector_state)
    
    

    # Check if init_vector_state and target_vector_state are opposite
    if np.allclose(init_vector_state, -target_vector_state):
        if init_vector_state[0] == 0 or target_vector_state[0] == 0:
            rx_angle = np.pi
            ry_angle = 0
            rz_angle = 0
        elif init_vector_state[1] == 0 or target_vector_state[1] == 0:
            rx_angle = 0
            ry_angle = np.pi
            rz_angle = 0
        elif init_vector_state[2] == 0 or target_vector_state[2] == 0:
            rx_angle = 0
            ry_angle = 0
            rz_angle = np.pi

    # Tạo mạch lượng tử và áp dụng cổng xoay
    qc = QuantumCircuit(1)
    qc.rx(rx_angle, 0)
    qc.ry(ry_angle, 0)
    qc.rz(rz_angle, 0)

    # Hiển thị mạch lượng tử và quá trình chuyển động
    qc.draw('mpl')
    plt.show()

    if SAVE_ANIMATE_TO_FILE:
        visualize_transition(qc, trace=True, saveas=ANIMATE_FILE_NAME, fpg=FPG_ANIMATE, spg=SPG_ANIMATE, init_vector_state=init_vector_state)
    else:
        visualize_transition(qc, trace=True, fpg=FPG_ANIMATE, spg=SPG_ANIMATE, init_vector_state=init_vector_state)