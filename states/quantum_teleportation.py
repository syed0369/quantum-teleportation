from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator
from collections import defaultdict

def teleportation_circuit(bit):
    
    data = QuantumRegister(1, "data")
    sender = QuantumRegister(1, "sender")
    receiver = QuantumRegister(1, "receiver")

    classical_bits = ClassicalRegister(3, "c")

    circuit = QuantumCircuit(data, sender, receiver, classical_bits)

    if bit == '1':
        circuit.x(data)

    circuit.h(sender)
    circuit.cx(sender, receiver)

    circuit.barrier()

    circuit.cx(data, sender)
    circuit.h(data)

    circuit.barrier()

    circuit.measure(data, classical_bits[0])
    circuit.measure(sender, classical_bits[1])

    circuit.barrier()

    with circuit.if_test((classical_bits[1], 1)):
        circuit.x(receiver[0])

    with circuit.if_test((classical_bits[0], 1)):
        circuit.z(receiver[0])

    circuit.measure(receiver[0], classical_bits[2])

    sim = AerSimulator()
    result = sim.run(circuit, shots=1000).result()
    counts = result.get_counts()

    result = defaultdict(int)

    for key, value in counts.items():
        first_bit = key[0]
        result[first_bit] += value
    
    if result['0'] > result['1']:
        return '0'
    
    return '1'


if __name__ == "__main__":
    text = input("Enter string: ")

    binary = ' '.join(format(ord(c), '08b') for c in text)
    binary_teleported = ""
    for bit in binary:
        if bit == '1' or bit == '0':
            binary_teleported += teleportation_circuit(bit)
        else:
            binary_teleported += bit
    teleported = ''.join(chr(int(b, 2)) for b in binary_teleported.split())
    print(f"Original text: {text}")
    print(f"Teleported text: {teleported}")