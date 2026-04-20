from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create Bell circuit
def phi_plus():
    bell = QuantumCircuit(2)
    bell.h(0)
    bell.cx(0, 1)
    bell.measure_all()
    return bell
def phi_minus():
    bell = QuantumCircuit(2)
    bell.x(0)
    bell.h(0)
    bell.cx(0, 1)
    bell.measure_all()
    return bell
def psi_plus():
    bell = QuantumCircuit(2)
    bell.x(1)
    bell.h(0)
    bell.cx(0, 1)
    bell.measure_all()
    return bell
def psi_minus():
    bell = QuantumCircuit(2)
    bell.h(0)
    bell.x(1)
    bell.z(0)
    bell.z(1)
    bell.cx(0, 1)
    bell.measure_all()
    return bell

def get_circuit_and_measurement(bell_state):
    sim = AerSimulator()
    result = sim.run(bell_state, shots=1000).result()
    counts = result.get_counts()

    # Create plots - 
    #   1. quantum circuit
    #   2. measurement stats for 1000 shots
    _, axes = plt.subplots(1, 2, figsize=(12, 5))


    bell_state.draw("mpl", ax=axes[0])
    axes[0].set_title("Bell Circuit")

    plot_histogram(counts, ax=axes[1])
    axes[1].set_title("Measurement Results")

    plt.tight_layout()
    plt.show()
