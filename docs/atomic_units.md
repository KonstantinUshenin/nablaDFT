# Atomic units

nablaDFT provides you several interfaces to work with the data.

You can access to Hamiltonian records using the `HamiltonianDatabase` dataloader:
```python
from nablaDFT.dataset import HamiltonianDatabase

train = HamiltonianDatabase("dataset_train_2k.db")
Z, R, E, F, H, S, C = train[0]  # atoms numbers, atoms positions, energy, forces, core hamiltonian, overlap matrix, coefficients matrix
```

| Index | Meaning            | Size of tensor | Physical units      | Data types |   |
|-------|--------------------|----------------|---------------------|------------|---|
| 0     | Atom numbers       | (N)            |                     | int32        |   |
| 1     | Atom positions     | (N, 3)         | Bohr                | float32    |   |
| 2     | Energy             | (1)            | Eh  (Hartree units) | float32    |   |
| 3     | Forces             | (N, 3)         | Eh/Bohr             | float64    |   |
| 4     | Hamiltonian        | (Norb, Norb)   |                     | float32    |   |
| 5     | Overlap matrix     | (Norb, Norb)   |                     | float32    |   |
| 6     | Coefficient matrix | (Norb, Norb)   |                     | float64    |   |
|       |                    |                |                     |            |   |
|       |                    |                |                     |            |   |
