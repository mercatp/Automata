#!/usr/bin/env sage-python27

from setuptools import setup, Extension
from codecs import open # To use a consistent encoding
from os import path
from Cython.Build import cythonize
import Cython.Compiler.Options
from sage.env import sage_include_directories

ext_modules = [
        Extension('automata.cautomata',
            sources = [path.join('automata','cautomata.pyx'),
                      path.join('automata','automataC.c'),
                      path.join('automata','cautomata.pyx'),],
            header = [path.join('automata','automataC.h'),
                      path.join('automata','cautomata.pxd'),
                      path.join('automata', 'Automaton.h')],
            include_dirs=sage_include_directories())]

# Get the long description from the README file)
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='Automata',
    version=open("VERSION").read().strip(),
    description="Tools to manipulate automata efficiently in Sage math. ",
    long_description=long_description,
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 0 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords='sagemath combinatorics automata deterministics automata',
    author='Paul Mercat and Dominique Benielli',
    author_email='paul.mercat[A]univ-amu.fr.antispam'+
                 'dominique.benielli[A]univ-amu.fr.antispam' ,
    install_requires=['numpy>=1.8', 'scipy>=0.16'],
    #install_requires=['cython','cysignals'], # this causes update of cysignals
                                              # which forces recompilation of all cython files!
    #url='http://www.slabbe.org/Sage',
    url='http://github.com/mercatp/Automata',
    license = "GPLv2+",
    packages=['automata'],
    ext_modules=cythonize(ext_modules),
)

