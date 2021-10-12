# PyMTP

Python wrapper to [moment tensor potential](https://gitlab.com/ashapeev/mlip-2).

## Install

First install [mlip-2](https://gitlab.com/ashapeev/mlip-2), then follow the steps below to install:

```bash
export MLIP_DIR="path-to-mlip-2" 
# e.g. "/Users/hello/mlip-2"
export MLIP_LIB="path-to-lib_mlip_interface.a" 
# e.g.  /Users/hello/opt/mlip-2/lib/lib_mlip_interface.a
```

```bash
# gcc
CC=gcc-11 CXX=g++-11 pip install . -v

# intel
CC=icpc CXX=icpc pip install . -v
```

## Usage

```python
from pymtp.core import MTPCalactor
from pymtp.core import PyConfiguration
from ase.io import read

a0 = read("POSCAR")

c0 = PyConfiguration.from_ase_atoms(a0)
calc = MTPCalactor("pot.mtp")
calc.calc(c0)

print(c0.energy)
print(c0.force)
print(c0.stresses)
```