# Atomic units

## Databases

You can access to Hamiltonian records using the `HamiltonianDatabase` dataloader:
```python
from nablaDFT.dataset import HamiltonianDatabase

train = HamiltonianDatabase("dataset_train_2k.db")
Z, R, E, F, H, S, C = train[0]  # atoms numbers, atoms positions, energy, forces, core hamiltonian, overlap matrix, coefficients matrix
```

| Index | Meaning            | Size of tensor | Physical units      | Data types |   |
|-------|--------------------|----------------|---------------------|------------|---|
| 0     | Atom numbers       | (N)            | e                   | int32      |   |
| 1     | Atom positions     | (N, 3)         | Bohr                | float32    |   |
| 2     | Energy             | (1)            | Eh  (Hartree units) | float32    |   |
| 3     | Forces             | (N, 3)         | Eh/Bohr             | float64    |   |
| 4     | Hamiltonian        | (Norb, Norb)   |                     | float32    |   |
| 5     | Overlap matrix     | (Norb, Norb)   |                     | float32    |   |
| 6     | Coefficient matrix | (Norb, Norb)   |                     | float64    |   |
|       |                    |                |                     |            |   |
|       |                    |                |                     |            |   |


## Metainformation

Tha major part of metainformation and additional information about molecules are included into `summary.csv`.

| Column name                  | Meaning | Size of tensor       | Physical units | Data types |
|------------------------------|---------|----------------------|----------------|------------|
| MOSES id                     |         |                      | int64          |            |
| CONFORMER id                 |         |                      | int64          |            |
| archive name                 |         |                      | str            |            |
| SMILES                       |         |                      | str            |            |
| DFT TOTAL ENERGY             |         | Eh  (Hartree units)  | float32        |            |
| DFT XC ENERGY                |         | Eh  (Hartree units)  | float32        |            |
| DFT NUCLEAR REPULSION ENERGY |         | Eh  (Hartree units)  | float32        |            |
| DFT ONE-ELECTRON ENERGY      |         | Eh  (Hartree units)  | float32        |            |
| DFT TWO-ELECTRON ENERGY      |         | Eh  (Hartree units)  | float32        |            |
| DFT DIPOLE X                 |         | Eh  (Hartree units)  | float32        |            |
| DFT DIPOLE Y                 |         | Eh  (Hartree units)  | float32        |            |
| DFT DIPOLE Z                 |         | Eh  (Hartree units)  | float32        |            |
| DFT TOTAL DIPOLE             |         | Eh  (Hartree units)  | float32        |            |
| DFT ROT CONSTANT A           |         | Eh  (Hartree units)  | float32        |            |
| DFT ROT CONSTANT B           |         | Eh  (Hartree units)  | float32        |            |
| DFT ROT CONSTANT C           |         | Eh  (Hartree units)  | float32        |            |
| DFT HOMO                     |         | Eh  (Hartree units)  | float32        |            |
| DFT LUMO                     |         | Eh  (Hartree units)  | float32        |            |
| DFT HOMO-LUMO GAP            |         | Eh  (Hartree units)  | float32        |            |
| DFT ATOMIC ENERGY            |         | Eh  (Hartree units)  | float32        |            |
| DFT FORMATION ENERGY         |         | Eh  (Hartree units)  | float32        |            |

# ATOMIC, FORMATION energy дополнительно посчитаны нами
