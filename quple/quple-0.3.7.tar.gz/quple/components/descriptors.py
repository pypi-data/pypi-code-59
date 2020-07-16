import cirq
import numpy as np
from itertools import combinations
from pdb import set_trace

#reference: https://github.com/tensorflow/quantum/blob/v0.3.0/tensorflow_quantum/python/util.py
def _symbols_in_op(op):
    """Returns the set of symbols in a parameterized gate."""
    if isinstance(op, cirq.EigenGate):
        return op.exponent.free_symbols

    if isinstance(op, cirq.FSimGate):
        ret = set()
        if isinstance(op.theta, sympy.Basic):
            ret |= op.theta.free_symbols
        if isinstance(op.phi, sympy.Basic):
            ret |= op.phi.free_symbols
        return ret

    if isinstance(op, cirq.PhasedXPowGate):
        ret = set()
        if isinstance(op.exponent, sympy.Basic):
            ret |= op.exponent.free_symbols
        if isinstance(op.phase_exponent, sympy.Basic):
            ret |= op.phase_exponent.free_symbols
        return ret

    raise ValueError("Attempted to scan for symbols in circuit with unsupported"
                     " ops inside. Expected op found in tfq.get_supported_gates"
                     " but found: ".format(str(op)))

#reference: https://github.com/tensorflow/quantum/blob/v0.3.0/tensorflow_quantum/python/util.py
def get_circuit_symbols(circuit):
    all_symbols = set()
    for moment in circuit:
        for op in moment:
            if cirq.is_parameterized(op):
                all_symbols |= _symbols_in_op(op.gate)
    return sorted([str(x) for x in all_symbols])


def sample_final_states(circuit, samples=1):
    import tensorflow_quantum as tfq
    layer = tfq.layers.State()
    symbols = get_circuit_symbols(circuit)
    if symbols:
        data = np.random.rand(samples,len(symbols))*2*np.pi
        tensor_final_states = layer(circuit, symbol_names=symbols, symbol_values=data)
    else:
        tensor_final_states = layer([circuit]*samples)
    final_states = [tensor_state.numpy() for tensor_state in tensor_final_states]
    return final_states

def sample_density_matrices(circuit, samples=1):
    final_states = sample_final_states(circuit, samples)
    density_matrices = [cirq.density_matrix_from_state_vector(fs) for fs in final_states] 
    return density_matrices


def sample_fidelities(circuit, samples = 1):
    sample_states_1 = sample_final_states(circuit, samples)
    sample_states_2 = sample_final_states(circuit, samples)
    fidelities = []
    for s1, s2 in zip(sample_states_1, sample_states_2):
        fidelities.append(cirq.fidelity(s1, s2))
    return fidelities

def circuit_fidelity_pdf(circuit, samples=3000, bins=100):
    data = np.array(sample_fidelities(circuit, samples))
    pdf = np.histogram(data, bins=bins, range=(0,1), density=True)
    return pdf

def Haar_pdf(samples=3000, bins=100):
    data = np.random.uniform(size=(samples))
    pdf = np.histogram(data, bins=bins, range=(0.,1.), density=True)
    return pdf

def circuit_fidelity_plot(circuit, samples=3000, bins=100, KL=True):
    import matplotlib.pyplot as plt
    data_pqc = np.array(sample_fidelities(circuit, samples))
    daa_Haar = np.random.uniform(size=(samples))
    plt.hist(data_pqc, bins=bins, range=(0.,1.), alpha=0.5, density=True, label='PQC')
    plt.hist(daa_Haar, bins=bins, range=(0.,1.), alpha=0.5, density=True, label='Haar')
    plt.legend()
    plt.xlabel('Fidelity')
    plt.ylabel('Probability')
    if KL:
        import scipy as sp
        pdf_pqc = np.histogram(data_pqc, bins=bins, range=(0.,1.), density=True)
        pdf_Haar = np.histogram(daa_Haar, bins=bins, range=(0.,1.), density=True)
        Kullback_Leibler_divergence = sp.stats.entropy(pdf_pqc[0], pdf_Haar[0])
        plt.title('$D_{KL}=$'+str(Kullback_Leibler_divergence))
    return plt

def circuit_expressibility_measure(circuit, samples = 3000, bins=100):
    import scipy as sp
    pdf_pqc = circuit_fidelity_pdf(circuit, samples, bins)
    pdf_Haar = Haar_pdf(samples, bins)
    Kullback_Leibler_divergence = sp.stats.entropy(pdf_pqc[0], pdf_Haar[0])
    return Kullback_Leibler_divergence

def Meyer_Wallach_measure(state):
    state = np.array(state)
    size = state.shape[0]
    n = int(np.log2(size))
    Q = 0.
    def linear_mapping(b:int, j:int) -> np.ndarray:
        keep_indices = [i for i in range(size) if b == ((i & (1 << j))!=0)]
        return state[keep_indices]
    def distance(u:np.ndarray, v:np.ndarray) -> float:
        assert u.shape == v.shape
        assert (u.ndim == 1) and (v.ndim == 1)
        D = 0.
        pairs = combinations(range(u.shape[0]), 2)
        for i,j in pairs:
            D += np.abs(u[i]*v[j] - u[j]*v[i])**2
        return D
    for k in range(n):
        iota_0k = linear_mapping(0, k)
        iota_1k = linear_mapping(1, k)
        Q += distance(iota_0k, iota_1k)
    Q = (4/n)*Q
    return Q
    
        
def circuit_entangling_measure(circuit, samples=200):
    final_states = sample_final_states(circuit, samples)
    mw_measures = [Meyer_Wallach_measure(fs) for fs in final_states]
    return np.mean(mw_measures)


def circuit_von_neumann_entropy(circuit, samples=200):
    density_matrices = sample_density_matrices(circuit, samples)
    von_neumann_entropy = [cirq.von_neumann_entropy(dm) for dm in density_matrices]
    return np.mean(von_neumann_entropy)
    
    
def gradient_variance_test(circuits, op, symbol=None):
    import tensorflow_quantum as tfq
    import tensorflow as tf
    """Compute the variance of a batch of expectations w.r.t. op on each circuit that 
    contains `symbol`."""
    resolved_circuits = []
    # Resolve irrelevant symbols:
    for circuit in circuits: 
        symbols = get_circuit_symbols(circuit)
        if not len(symbols) > 0:
            raise ValueError('No symbols found in circuit')
        if not symbol:
            symbol = symbols[0]
            symbols = symbols[1:]
        else:
            symbols.remove(symbol)
        resolver = cirq.ParamResolver({s:np.random.uniform() * 2.0 * np.pi for s in symbols})
        resolved_circuits.append(cirq.protocols.resolve_parameters(circuit, resolver))

    # Setup a simple layer to batch compute the expectation gradients.
    expectation = tfq.layers.Expectation()

    # Prep the inputs as tensors
    circuit_tensor = tfq.convert_to_tensor(resolved_circuits)
    n_circuits = len(resolved_circuits)
    values_tensor = tf.convert_to_tensor(
        np.random.uniform(0, 2 * np.pi, (n_circuits, 1)).astype(np.float32))

    # Use TensorFlow GradientTape to track gradients.
    with tf.GradientTape() as g:
        g.watch(values_tensor)
        forward = expectation(circuit_tensor,
                              operators=op,
                              symbol_names=[symbol],
                              symbol_values=values_tensor)

    # Return variance of gradients across all circuits.
    grads = g.gradient(forward, values_tensor)
    grad_var = tf.math.reduce_std(grads, axis=0)
    return grad_var.numpy()[0]

