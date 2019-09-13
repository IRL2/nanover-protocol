#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_namespace_packages

setup(name='narupa-ase',
      version='0.1.0',
      description='ASE integration for Narupa',
      author='Intangible Realities Lab',
      author_email='m.oconnor@bristol.ac.uk',
      url='https://gitlab.com/intangiblerealities/',
      packages=find_namespace_packages('src', include='narupa.*'),
      package_dir={'': 'src'},
      install_requires=(
          'narupa',
          'ase',
      ),
      entry_points={
          'console_scripts': ['narupa-omm-ase=narupa.ase.openmm.cli:main'],
      },
      )
