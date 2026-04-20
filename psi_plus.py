from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create Bell circuit
def bell_state():
    bell = QuantumCircuit(2)
    bell.h(0)
    bell.x(1)
    bell.cx(0, 1)
    bell.measure_all()
    return bell

# Run simulation
bell = bell_state()
sim = AerSimulator()
result = sim.run(bell, shots=1000).result()
counts = result.get_counts()

# Create plots - 
#   1. quantum circuit
#   2. measurement stats for 1000 shots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))


bell.draw("mpl", ax=axes[0])
axes[0].set_title("Bell Circuit")

plot_histogram(counts, ax=axes[1])
axes[1].set_title("Measurement Results")

plt.tight_layout()
plt.show()