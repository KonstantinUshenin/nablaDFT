import os
import io

from setuptools import setup, find_packages


CUDA = "cu121"


def read(fname):
    with io.open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()



setup(
    name="nablaDFT",
    version="2.0.0",
    author="Khrabrov, Kuzma and Shenbin, Ilya and Ryabov, Alexander and Tsypin, Artem and Telepov, Alexander and Alekseev, Anton and Grishin, Alexander and Strashnov, Pavel and Zhilyaev, Petr and Nikolenko, Sergey and Kadurin, Artur",
    url="https://github.com/AIRI-Institute/nablaDFT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.26",
        "sympy==1.12",
        "ase==3.22.1",
        "h5py==3.10.0",
        "apsw==3.45.1.0",
        "schnetpack==2.0.4",
        "tensorboardX",
        "pyyaml",
        "hydra-core==1.2.0",
        "torch==2.2.0",
        "torch-scatter @ https://data.pyg.org/whl/torch-2.2.0+${CUDA}.html",
        "torch-sparse @ https://data.pyg.org/whl/torch-2.2.0+${CUDA}.html",
        "torch-cluster @ https://data.pyg.org/whl/torch-2.2.0+${CUDA}.html",
        "pytorch_lightning==2.1.4",
        "torch-geometric==2.4.0",
        "torchmetrics==1.0.1",
        "hydra-colorlog>=1.1.0",
        "rich",
        "fasteners",
        "dirsync",
        "torch-ema==0.3",
        "matscipy",
        "python-dotenv",
        "wandb==0.16.3",
        "e3nn==0.5.1"
    ],
    license="MIT",
    description="nablaDFT: Large-Scale Conformational Energy and Hamiltonian Prediction benchmark and dataset",
    long_description="""
        Electronic wave function calculation is a fundamental task of computational quantum  chemistry. Knowledge of the wave function parameters allows one to compute physical and chemical properties of molecules and materials.
        In this work we: introduce a new curated large-scale dataset of electron structures of drug-like molecules, establish a novel benchmark for the estimation of molecular properties in the multi-molecule setting, and evaluate a wide range of methods with this benchmark.""",
)
