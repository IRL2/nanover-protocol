# NanoVer 2 Protocol

Repository containing the gRPC protocol and python based implementations
of servers for NanoVer, providing a framework for developing interactive molecular dynamics simulations.

It is designed to be used with **NanoVer VR clients**, e.g. [NanoVer IMD](https://github.com/irl2/nanover-imd).

This repository is maintained by the Intangible Realities Laboratory, University of Santiago de Compostela,
and distributed under the [MIT](LICENSE) license.
See [the list of contributors](CONTRIBUTORS.md) for the individual authors of the project.

For more information please take a look at [the project's documentation](https://irl2.github.io/nanover-docs/#).

## Contents

1. [Getting started](#Getting-started)
2. [User installation](#User-installation)
3. [Developer installation](#Developer-installation)
4. [Troubleshooting](#Troubleshooting)
5. [Citation and external libraries](#Citation-and-external-libraries)

----

## Getting started

### Quick start

`nanover.omni` provides a command line interface for running OpenMM simulations. For example, from the `nanover-protocol` directory:

    nanover-omni --omm examples/ase/openmm_files/nanotube.xml

Learn more about running a NanoVer server 
[here](https://irl2.github.io/nanover-docs/tutorials/fundamentals.html#running-a-server) in our documentation.

### Tutorials

The [examples](examples) folder contains [Jupyter notebooks](https://jupyter.org/) for getting started with NanoVer. 
Please head to the [Tutorials](https://irl2.github.io/nanover-docs/tutorials) page of the 
[project's documentation](https://irl2.github.io/nanover-docs) for more information!


### Exploring the code  

The `protocol` folder contains the definitions of the gRPC services.

The `python-libraries` folder contains the library to write NanoVer clients and
servers in python, as well as the services implemented in python. The
`python-libraries/prototypes` directory contains examples and (sometimes
unmaintained) prototypes using the python libraries.

The `csharp-libraries/NanoVer.Protocol` folder contains C# implementations of clients for receiving trajectories and structures.

## User installation

Check out the [Installation & Getting Started](https://irl2.github.io/nanover-docs/installation) 
age in our documentation for detailed instructions on installing NanoVer.

#### Updating ####

* Run `conda list ^nanover-server` to determine the currently installed version
* Run `conda install nanover-server` to attempt to update to latest version
* If you can't seem to update to the latest version, run `python --version` to check your python version is at least as recent as in these installation instructions. If it isn't you will need to create a new conda environment with a newer version of python.


## Developer installation

### Windows

* Install Anaconda
* Install the .NET core SDK (see <https://dotnet.microsoft.com/download>)
* Clone the nanover-protocol repository
* In the "Anaconda Powershell Prompt":
    * Create a conda environment (here we call the environment "nanover-dev"): `conda create -n nanover-dev "python>3.11"`
    * Activate the conda environment: `conda activate nanover-dev`
    * Install the required conda packages: `conda install -c conda-forge openmm MDAnalysis MDAnalysisTests ase`
    * Compile the protocol and install the NanoVer libraries in your conda environment: `./win_compile.ps1`.  If you do not plan on modifying the python packages, run `./win_compile.ps1 -noedit` instead. Otherwise, by default, the nanover packages will be installed in edit mode (`pip install -e`) meaning that changes in the `nanover-protocol` directory will be directly reflected in your python environment.
* The `nanover-lammps` module and its tests require MPI to be installed. Download and install Microsoft MPI from https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi

### Mac and Linux

* Install Anaconda
* Clone the nanover-protocol repository
* In a terminal, in the repository root:
    * Create a conda environment (here we call the environment "nanover-dev"): `conda create -n nanover-dev "python>3.11"`
    * Activate the conda environment: `conda activate nanover-dev`
    * Install the required conda package: `conda install -c conda-forge openmm MDAnalysis MDAnalysisTests ase mpi4py`
    * Compile the protocol and install the NanoVer python libraries in your conda environment: `./compile.sh --no-dotnet`.  If you do not plan on modifying the python packages, you may run `./compile.sh --no-edit --no-dotnet` instead. Otherwise, by default, the NanoVer packages will be installed in edit mode (`pip install -e`) meaning that changes in the `nanover-protocol` directory will be directly reflected in your python environment.

Here, we installed only the python library. Using the `--no-dotnet` argument, we skipped building the C# libraries for NanoVer. Would you want to work on these library, you would need to:

* Install dotnet 2.11. This is an old version of the framework that is not maintained anymore. However, Unity still relies on it.
* Run the compile script: `./compile.sh --no-python` to skip installing the python libraries, or just `./compile.sh` to build the python libraries as well.


### Running the tests

All code changes have to pass a series of automatic tests ("the CI") that attempt to verify code quality and
continued functionality of the project. You can run these locally to verify your changes in advance.

#### Unit Tests

The unit tests check code functionality of the python libraries. To run them:

    python -m pytest python-libraries

Optionally, you can run most of the tests in parallel with pytest-xdist:

    python -m pip install pytest-xdist
    python -m pytest python-libraries -n auto -m 'not serial'
    python -m pytest python-libraries -n0 -m 'serial'

#### Formatting & Linting Tests

The formatting and linting tests check code style, and require ruff and black:

    python -m pip install ruff
    python -m pip install black
    python -m ruff check python-libraries
    python -m black --diff --check python-libraries

black can automatically reformat the files for you:

    python -m black python-libraries

#### Type Checks

The type checks look at the type hints in the code to make sure they are consistent and help find potential errors. 
Because of the special setup required you will probably not be able to run this locally, but you can try:

    python -m pip install mypy
    packages=$(find python-libraries -name __init__.py \ 
             | sed 's/__init__.py//g' \ 
             | awk '{split($0, a, /src/); print(a[2])}' \ 
             | sed 's#/#.#g' \ 
             | cut -c 2- \ 
             | sed 's/\.$//g' \ 
             | grep -v '^$' \ 
             | grep -v protocol \ 
             | sed 's/^/-p /g' \ 
             | grep -v '\..*\.' \ 
             | tr '\n' ' ') 
    python -m mypy --ignore-missing-imports --namespace-packages --check-untyped-defs --allow-redefinition $packages 

### Running the examples

#### OpenMM IMD Simulations

`nanover.omni` provides a command line interface for running serialised OpenMM simulations. For example, from the 
`nanover-protocol` directory:

    nanover-omni --omm examples/ase/openmm_files/nanotube.xml

#### ASE IMD Simulations Jupyter Notebooks

The [`examples/ase`](examples/ase) folder contains several Jupyter notebooks that demonstrate visualisation and interaction 
from a notebook. The [NanoVer ASE documentation](python-libraries/nanover-ase/README.md) provides more details on setting 
up ASE simulations.

#### MD Analysis Trajectories

`nanover.mdanalysis` provides a server for the trajectory service that infinitely loops over the frames of an example
trajectory. To serve the frames on port 54321, from the `nanover-protocol` directory, run

    python ./examples/mdanalysis/example.py

## Troubleshooting

### Autoconnect

If you are having autoconnecting to servers, you can run `nanover-essd-list` to verify which local network servers are visible to your machine.

## Citation and external libraries

If you find this project useful, please cite the following papers:

> Jamieson-Binnie, A. D., O’Connor, M. B., Barnoud, J., Wonnacott, M. D., Bennie, S. J., & Glowacki, D. R. (2020, August 17). Narupa iMD: A VR-Enabled Multiplayer Framework for Streaming Interactive Molecular Simulations. ACM SIGGRAPH 2020 Immersive Pavilion. SIGGRAPH ’20: Special Interest Group on Computer Graphics and Interactive Techniques Conference. https://doi.org/10.1145/3388536.3407891

> M. O’Connor, S.J. Bennie, H.M. Deeks, A. Jamieson-Binnie, A.J. Jones, R.J. Shannon, R. Walters, T. Mitchell, A.J. Mulholland, D.R. Glowacki, [“Interactive molecular dynamics from quantum chemistry to drug binding: an open-source multi-person virtual reality framework”](https://aip.scitation.org/doi/10.1063/1.5092590), J. Chem Phys 150, 224703 (2019)

This project has been made possible by the following open source projects. We gratefully thank them for their efforts, and suggest that you use and cite them:

* [gRPC](https://grpc.io/) (Apache v2) - Communication protocol.
* [ASE](https://wiki.fysik.dtu.dk/ase/) (LGPLv3): Atomic simulation environment used for running simulations ([citation](https://iopscience.iop.org/article/10.1088/1361-648X/aa680e)).
* [OpenMM](http://openmm.org/) (MIT, LGPLv3): GPU accelerated molecular mechanics library ([citation](https://simtk.org/plugins/publications/index.php/?group_id=161)).
* [LAMMPS](https://lammps.sandia.gov/) (GPLv2): Molecular mechanics library ([citation](https://lammps.sandia.gov/cite.html)).
* [MDAnalysis](https://www.mdanalysis.org/) (GPLv2): Molecular dynamics analysis library ([citations](https://www.mdanalysis.org/pages/citations/)).
* [python-osc](https://pypi.org/project/python-osc/) (Public domain) - Open sound control library.
* [MPI4Py](https://mpi4py.readthedocs.io/en/stable/index.html) ([BSD 2-clause license](https://bitbucket.org/mpi4py/mpi4py/src/master/LICENSE.rst)): MPI library for python, used with LAMMPS ([citation](https://mpi4py.readthedocs.io/en/stable/citing.html)).
* [Numpy](https://numpy.org/) (BSD) - Numerical computation library.
* [Netifaces](https://pypi.org/project/netifaces/) (MIT) - Portable library for accessing network interface information.
* [Pytest](https://docs.pytest.org/en/latest/) (MIT) - Python testing framework
* [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) ([Mozilla Public License 2.0](https://github.com/HypothesisWorks/hypothesis/blob/master/hypothesis-python/LICENSE.txt)) - Python testing framework.
