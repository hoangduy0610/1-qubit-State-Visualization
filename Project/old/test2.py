import numpy as np
from qiskit import Aer, QuantumCircuit, execute
from qiskit.visualization import plot_bloch_multivector

# Prompt the user to enter a list of qubit states
qubit_states = input("Enter a list of qubit states (separated by spaces): ").split()

# Convert the qubit states to complex numbers
complex_states = [complex(state) for state in qubit_states]

# Normalize the complex states
normalized_states = np.array(complex_states) / np.linalg.norm(complex_states)

# Create a quantum circuit with the given qubit states
qc = QuantumCircuit(len(normalized_states))
qc.initialize(normalized_states, range(len(normalized_states)))

# Simulate the quantum circuit and get the final state vector
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
statevector = result.get_statevector()

# Plot the Bloch sphere for each qubit state
for i, state in enumerate(statevector):
    print(f"Qubit {i+1} state:")
    plot_bloch_multivector(state)
