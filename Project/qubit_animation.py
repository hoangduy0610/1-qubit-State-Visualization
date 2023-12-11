import sys

import numpy as np
from plotter import calculate_phi_and_theta
from animate import visualization
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 qubit_animation.py \"<initial_state>\" \"<target_state>\"")
        sys.exit(1)

    InitialState = sys.argv[1]
    TargetState = sys.argv[2]
    
    iState = InitialState.split(' ')
    tState = TargetState.split(' ')

    initial_state = np.array([float(string) for string in iState])
    target_state = np.array([float(string) for string in tState])

    
    theta, phi = calculate_phi_and_theta(initial_state[0], initial_state[1])
    initial_state = np.array([theta, phi])

    theta, phi = calculate_phi_and_theta(target_state[0], target_state[1])
    target_state = np.array([theta, phi])

    visualization(initial_state, target_state)
