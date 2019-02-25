#!/usr/bin/env sage-python27
# try:     
#     from sage.env import SAGE_SRC, SAGE_VERSION 
# except ImportError:
#     raise ValueError("this package currently installs only inside SageMath (http://www.sagemath.org)\n"                      "If you are using Ubuntu with Sage installed from the official apt repository, run\n"                      "first in a console \"$ source /usr/share/sagemath/bin/sage-env\"\n") 
# import re, os, sys
# import shutil
# from distutils.core import setup, Extension
# from distutils.command.clean import clean as _clean
# from distutils.dir_util import remove_tree
# from distutils.command.sdist import sdist
# import cysignals 
# #CYSIGNALS_SRC = cysignals.__path__[0]
# try:
#     from Cython.Distutils import build_ext
# except:
#     USE_CYTHON = False
#     raise 'Cannot build iw without cython'
#     sys.exit()
# relist = ['^.*~$', '^#.*#$', '^.*\.aux$', '^.*\.pyc$', '^.*\.o$']
# reclean = []
# USE_COPYRIGHT = True
# 
# try:
#     from copyright import writeStamp, eraseStamp
# except ImportError:
#     USE_COPYRIGHT = False
# try:
#     import numpy
# except:
#     raise 'Cannot build Automata without numpy'
#     sys.exit()
# #from setuptools import setup, Extension
# from distutils.core import setup 
# from distutils.extension import Extension
# from codecs import open # To use a consistent encoding
# from os import path
# from Cython.Build import cythonize
# import Cython.Compiler.Options
# from sage.env import sage_include_directories
#
# PATH_INCLUDES = [numpy.get_include(), '.', './automata']
# PATH_LIBRARIES = ['build', '.']
# LINK_LIBRARIES = ["m", ]
#
# EXTRA_COMPIL_ARGS = ['-g', ]
# ###################
# # Get Automata version
# ####################
# def get_version():
#     v_text = open('VERSION').read().strip()
#     v_text_formted = '{"' + v_text.replace('\n', '","').replace(':', '":"')
#     v_text_formted += '"}'
#     v_dict = eval(v_text_formted)
#     return v_dict["automata"]
# ########################
# # Set Automata __version__
# ########################
# def set_version(aut_dir, version):
#     filename = os.path.join(aut_dir, '__init__.py')
#     buf = ""
#     for line in open(filename, "rb"):
#         if not line.decode("utf8").startswith("__version__ ="):
#             buf += line.decode("utf8")
#     f = open(filename, "wb")
#     f.write(buf.encode("utf8"))
#     f.write(('__version__ = "%s"\n' % version).encode("utf8"))
# 
# for restring in relist:
#     reclean.append(re.compile(restring))
# def wselect(args, dirname, names):
#     for n in names:
#         for rev in reclean:
#             if (rev.match(n)):
#                 os.remove("%s/%s" %(dirname, n))
#         break
# ######################
# # Custom clean command
# ######################
# class clean(_clean):
#     def walkAndClean(self):
#         os.walk("..", wselect, [])
#         pass
# 
#     def run(self):
#         clean.run(self)
#         if os.path.exists('build'):
#             shutil.rmtree('build')
#         for dirpath, dirnames, filenames in os.walk('automata'):
#             for filename in filenames:
#                 if (filename.endswith('.so') or
#                         filename.endswith('.pyd') or
#                         filename.endswith('.dll') or
#                         filename.endswith('.pyc')):
#                     os.unlink(os.path.join(dirpath, filename))
#             for dirname in dirnames:
#                 if dirname == '__pycache__':
#                     shutil.rmtree(os.path.join(dirpath, dirname))
# ##############################
# # Custom sdist command
# ##############################
# class m_sdist(sdist):
#     """ Build source package
# 
#     WARNING : The stamping must be done on an default utf8 machine !
#     """
# 
#     def run(self):
#         if USE_COPYRIGHT:
#             writeStamp()
#             sdist.run(self)
#             # eraseStamp()
#         else:
#             sdist.run(self)
# 
# 
# ##########################
# # File path read command
# ##########################
# def read(*paths):
#     """Build a file path from *paths* and return the contents."""
#     with open(os.path.join(*paths), 'r') as f:
#         return f.read()
# 
# 
# 
# 
# ext_modules = [
#         Extension('automata.cautomata',
#                    ['automata/cautomata.pyx', 'automata/automataC.c', ],
#                          include_dirs=PATH_INCLUDES,
#                          library_dirs=PATH_LIBRARIES,
#                          include_path=PATH_INCLUDES,
#                          libraries=LINK_LIBRARIES,
#                          extra_compile_args=EXTRA_COMPIL_ARGS,), ]
# ####################
# # Setup method
# ####################
# def setup_package():
#     """ Setup function"""
#     # set version
#     VERSION = get_version()
#     aut_dir = 'automata'
#     set_version(aut_dir, VERSION)
#     setup(
#          name="Automata",
#          version=VERSION,
#          description="Automata : Tools to manipulate automata efficiently in Sage math.",
#          author='Paul Mercat and Dominique Benielli',
#          author_email='paul.mercat[A]univ-amu.fr.antispam'+
#                  'dominique.benielli[A]univ-amu.fr.antispam' ,
#          packages=['automata',],
#          package_dir={'automata': 'automata',},
#          package_data={'automata': ['*.pxd', '*.h'] },
#          ext_modules=ext_modules,
#          install_requires=['numpy>=1.8', 'scipy>=0.16'],
# 
#          define_macros=[('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')],
#          compiler_directives={'embedsignature': True, 'linetrace': True,
#                               'binding': True, 'profile': True, },
#          cmdclass={'build_ext': build_ext, 'clean': clean, 'sdist': m_sdist},
#     )
# 
#   #       test_suite='nose.collector',
#   #       tests_require=['nose', 'coverage'],
# if __name__ == "__main__":
#     setup_package()

 #           sources = [path.join('automata','cautomata.pyx'),
 #                      path.join('automata','automataC.c'),
#                      path.join('automata','cautomata.pyx'),],
#             header = [path.join('automata', 'Automaton.h'),
#                        path.join('automata','automataC.h'),
#                       path.join('automata','cautomata.pxd')],
#            include_dirs= sage_include_directories() ,
#            depend = [path.join('automata', 'Automaton.h'),
 #                       path.join('automata','automataC.h'),
#                       path.join('automata','cautomata.pxd')],
#)]
#[ os.path.join(SAGE_SRC, 'sage', 'libs', 'ntl'),  # apparently needed for Sage on archlinux   
 #                           os.path.join(SAGE_SRC, 'sage', 'cpython'),      # idem    
 #                           CYSIGNALS_SRC,                                  # idem              
  #                          'automata'                ]
# ext_modules = [ Extension('automata.cautomata',
#                             sources = ['cautomata.pyx', 'automataC.c'],
#                           header = ['Automaton.h','automataC.h' ,'cautomata.pxd'],
#                           dir =  'automata',
#                           include_dirs=sage_include_directories())
# ]
# 
#  Get the long description from the README file)
# #here = path.abspath(path.dirname(__file__))
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()
# 
# setup(name='Automata',
#     version=open("VERSION").read().strip(),
# #    description="Tools to manipulate automata efficiently in Sage math. ",
#     long_description=long_description,
#     classifiers=[
#       # How mature is this project? Common values are
#       #   3 - Alpha
# #      #   4 - Beta
#       #   5 - Production/Stable
#       'Development Status :: 0 - Beta',
#       'Intended Audience :: Science/Research',
#       'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
#       'Programming Language :: Python :: 2.7',
#       'Topic :: Scientific/Engineering :: Mathematics',
#     ],
#     keywords='sagemath combinatorics automata deterministics automata',
#     author='Paul Mercat and Dominique Benielli',
#     author_email='paul.mercat[A]univ-amu.fr.antispam'+
#                  'dominique.benielli[A]univ-amu.fr.antispam' ,
#     install_requires=['numpy>=1.8', 'scipy>=0.16'],
#     install_requires=['cython','cysignals'], # this causes update of cysignals
#                                              # which forces recompilation of all cython files!
#     #url='http://www.slabbe.org/Sage',
#     url='http://github.com/mercatp/Automata',
#     license = "GPLv2+",
#     packages=['automata'],
#     ext_modules=cythonize(ext_modules),
# )


#!/usr/bin/env bash
r"""
Installation script for the flatsurf module

It depends on distutils
"""

try:
    from sage.env import SAGE_SRC, SAGE_VERSION
except ImportError:
    raise ValueError("this package currently installs only inside SageMath (http://www.sagemath.org)#\n"
                      "If you are using Ubuntu with Sage installed from the official apt repository, run\n"
                      "first in a console \"$ source /usr/share/sagemath/bin/sage-env\"\n")

import cysignals
CYSIGNALS_SRC = cysignals.__path__[0]

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import sys, os
from distutils.version import LooseVersion

with open("VERSION") as f:
    v_text = f.read().strip()
    v_text_formted = '{"' + v_text.replace('\n', '","').replace(':', '":"')
    v_text_formted += '"}'
    v_dict = eval(v_text_formted)
    prefix = "version='"
    suffix = "'"
    version = v_dict["automata"]


with open("README.rst") as f:
    long_description = f.read()

try:
    import ppl
except ImportError:
    sys.stderr.write('Warning: pplpy not installed. Will not compile iet_family\n')
    WITH_PPL = False
else:
    WITH_PPL = True

extensions_data = {
     'automata': {
         'name': 'automata',
         'dir': os.path.join('.'),
         'sources': ['cautomata.pyx', 'automataC.c'],
         'headers': ['cautomata.pxd', 'automataC.h', 'Automata.h']
         },

 }

extensions = []
source_files = []

for name, data in extensions_data.items():
    if data.get('condition', True):
        print('Adding extension {}:\n  sources = {}\n  headers = {}'.format(data['name'], data['sources'], data['headers']))
        full_dir = os.path.join('automata', data['dir'])
        sources = [os.path.join(full_dir, src) for src in data['sources']]
        headers = [os.path.join(full_dir, data['dir'], head) for head in data['headers']]
        ext = Extension(data['name'],
            sources = sources,
            include_dirs =[SAGE_SRC, full_dir] + sys.path,
            depends = headers,
        )
        extensions.append(ext)
        sources = [os.path.join(data['dir'], src) for src in data['sources']]
        headers = [os.path.join(data['dir'], head) for head in data['headers']]
        source_files.extend(sources)
        source_files.extend(headers)


setup(name='Automata',
       version=version,
       description="Automata : Tools to manipulate automata efficiently in Sage math.",
       long_description=long_description,
       author='Paul Mercat and Dominique Benielli',
       author_email='paul.mercat[A]univ-amu.fr.antispam'+
                 'dominique.benielli[A]univ-amu.fr.antispam' ,
       url='http:///latest/',
       license="GPL v3",
       packages=['automata',],
       package_data={
           'automata': source_files,
           },
       ext_modules=cythonize(extensions),
       classifiers=[
       'Intended Audience :: Science/Research',
       'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
       'Operating System :: OS Independent',
       'Programming Language :: C',
       'Programming Language :: C++',
       'Programming Language :: Python',
       'Programming Language :: Cython',
       'Topic :: Scientific/Engineering :: Mathematics',
     ],
     keywords='sagemath combinatorics automata deterministics automata',
 )
