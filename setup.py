import os
import sys

from setuptools import setup, find_packages
from Cython.Distutils import build_ext
from setuptools.extension import Extension

# To use a consistent encoding
from codecs import open
from os import path
import numpy as np

environ = os.environ
MLIP_LIB = environ.get("MLIP_LIB", None)
MLIP_DIR = environ.get("MLIP_DIR", None)

if MLIP_DIR is None or MLIP_LIB is None:
    print("can't find MLIP_DIR and MLIP_LIB in environment of system.")
    sys.exit()
else:
    print(f"MLIP_LIB = {MLIP_LIB} \nMLIP_DIR={MLIP_DIR}\n\n")


mlip_include_dir = [
    f"{MLIP_DIR}/src/common",
    f"{MLIP_DIR}/src",
    f"{MLIP_DIR}/dev_src",
]
ext_modules = [
    Extension(
        "pymtp.core._mtp",
        # sources=["pymtp/core/_mtp.pyx"],
        sources=["pymtp/core/_mtp.cpp"],
        include_dirs=[np.get_include()] + mlip_include_dir,
        extra_objects=[MLIP_LIB],
        extra_compile_args=["-std=c++11"],
        extra_link_args=["-std=c++11"],
        language="c++",
    )
]


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


version = "1.0"
setup(
    name="pymtp",
    version=version,
    description="Python wrapper to moment tensor potential",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='hlyang',
    author_email='hlyang1992@gmail.com',
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=["numpy"],
    extras_require={"all": ["ase"]},
)
