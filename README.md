# Quantum Teleportation with Bell States

A comprehensive exploration of quantum entanglement and teleportation using IBM's Qiskit framework. This project demonstrates Bell states (maximally entangled two-qubit states) and implements the quantum teleportation protocol.

## Overview

This repository contains educational implementations of two fundamental quantum computing concepts:

1. **Bell States** - Generate and visualize all four maximally entangled Bell states (Φ⁺, Φ⁻, Ψ⁺, Ψ⁻)
2. **Quantum Teleportation** - Implement the quantum teleportation protocol to transmit quantum information

## Features

- 🔬 **Bell State Generation**: Create all four Bell states with customizable quantum circuits
- 📊 **Visualization**: Plot quantum circuits and measurement statistics from 1000-shot simulations
- 🚀 **Quantum Teleportation**: Teleport arbitrary quantum states using entanglement and classical communication
- 📝 **Text Encoding**: Encode and "teleport" text by converting to binary and applying the teleportation protocol

## Project Structure

```
├── states/
│   ├── bell_states.py          # Bell state circuits and visualizations
│   └── quantum_teleportation.py # Quantum teleportation implementation
├── requirements.txt             # Python dependencies
└── README.md                   # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bell-states
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Bell States

To visualize all four Bell states and their measurement results:

```python
from states.bell_states import phi_plus, phi_minus, psi_plus, psi_minus, get_circuit_and_measurement

# Create and visualize Bell state Φ⁺
bell_circuit = phi_plus()
get_circuit_and_measurement(bell_circuit)

# Other Bell states: phi_minus(), psi_plus(), psi_minus()
```

This will display:
- The quantum circuit diagram
- Measurement statistics from 1000 simulated shots

### Quantum Teleportation

To teleport text using the quantum teleportation protocol:

```bash
python states/quantum_teleportation.py
# Enter: Hello
# Output will show original and teleported text
```

The program:
1. Converts input text to 8-bit binary
2. Teleports each bit individually using the quantum teleportation protocol
3. Reconstructs and displays the teleported text

## Bell States Explained

Bell states are maximally entangled two-qubit states that form an orthonormal basis:

- **Φ⁺** (Phi-Plus): |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
- **Φ⁻** (Phi-Minus): |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
- **Ψ⁺** (Psi-Plus): |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
- **Ψ⁻** (Psi-Minus): |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2

These states show perfect quantum correlation - measuring one qubit instantly determines the state of the other.

## Quantum Teleportation Protocol

The teleportation circuit implements the standard protocol:

1. **Bell Pair Creation**: Sender and Receiver share an entangled pair
2. **Bell Measurement**: Sender performs Bell measurement on data qubit and their half of entangled pair
3. **Classical Communication**: Send 2 classical bits from measurement results
4. **Correction**: Receiver applies conditional gates based on classical bits
5. **Result**: Original quantum state is transferred to Receiver's qubit

## Dependencies

- **qiskit** (2.4.0) - Quantum circuit framework
- **qiskit-aer** (0.17.2) - High-performance quantum simulator
- **matplotlib** (3.10.8) - Visualization library
- **numpy** (2.4.4) - Numerical computing
- **scipy** (1.17.1) - Scientific computing

See `requirements.txt` for complete dependency list and versions.

## References

- [Qiskit Quantum Teleportation](https://quantum.cloud.ibm.com/learning/en/modules/computer-science/quantum-teleportation)Bell_state)

