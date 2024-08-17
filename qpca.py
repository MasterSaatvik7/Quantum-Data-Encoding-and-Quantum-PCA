from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import FidelityQuantumKernel
import numpy as np
import pandas as pd

def run_qiskit_qpca(data, n_components=2):
    data = np.array(data, dtype=float)
    if data.ndim != 2:
        raise ValueError("Data must be a 2D array.")

    feature_map = ZZFeatureMap(feature_dimension=data.shape[1], reps=2)
    quantum_kernel = FidelityQuantumKernel(feature_map=feature_map)
    
    # Compute the fidelity matrix
    fidelity_matrix = quantum_kernel.evaluate(data, data)
    
    # Perform eigen decomposition of the fidelity matrix
    eigenvalues, eigenvectors = np.linalg.eigh(fidelity_matrix)
    
    # Select the top components
    top_components = eigenvectors[:, -n_components:]
    reduced_data = np.dot(top_components.T, data ).T
    
    return reduced_data

def perform_quantum_pca(df, n_components: int = 2, method: str ='qiskit'):
    """
    Perform Quantum PCA using Qiskit on the provided DataFrame.

    Parameters:
    - df: DataFrame, the data on which to perform PCA
    - exclude_columns: List of columns to exclude from PCA
    - n_components: Integer, the number of principal components to reduce to
    - method: String, currently only 'qiskit' is supported

    Returns:
    - DataFrame containing the reduced components
    """

    data = df.values
    
    if method == 'qiskit':
        reduced_data = run_qiskit_qpca(data, n_components)
    else:
        raise ValueError("Currently only 'qiskit' method is supported")
    
    return pd.DataFrame(reduced_data, columns=[f'PC{i+1}' for i in range(n_components)])
