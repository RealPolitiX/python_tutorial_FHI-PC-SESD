# Python tutorial @ FHI-PC-SESD
Course materials for the internal python tutorial at Fritz Haber Institute's Physical Chemistry department  
**Lecturers**: Patrick Xian, Faruk Krecinic  
**Duration**: 4 lectures, each 1.5-2 hrs


[Rosetta stone](http://mathesaurus.sourceforge.net/matlab-numpy.html) for Matlab users picking up Python


### 0. System configuration: 
1. python installation (installed [Anaconda](https://www.continuum.io/) distribution before class)
2. package installation
3. [git](https://git-scm.com/)


### 1. Python basics (incl. the standard library) [:arrow_forward:](https://github.com/RealPolitiX/python_tutorial_FHI-PC-SESD/blob/master/materials/PyTutorial_01_Basics.ipynb)
1. python data types and operations
2. sys/os/glob/[glob2](https://pypi.python.org/pypi/glob2)  
3. time [py2](https://docs.python.org/2/library/time.html) | [py3](https://docs.python.org/3/library/time.html) 
4. itertools [py2](https://docs.python.org/2/library/itertools.html) | [py3](https://docs.python.org/3/library/itertools.html) 
5. functional vs. object-oriented programming in python
6. file i/o in scipy, pandas, [h5py](http://www.h5py.org/)


### 2. Development environment and platforms [:arrow_forward:](https://github.com/RealPolitiX/python_tutorial_FHI-PC-SESD/blob/master/materials/PyTutorial_02_Jupyter.ipynb)
1. [Jupyter](http://jupyter.org/)
2. [Spyder](https://github.com/spyder-ide/spyder) 
3. [PyCharm](https://www.jetbrains.com/pycharm/) 
4. [Atom](https://atom.io/)


### 3. Python numerics stack [:arrow_forward:](https://github.com/RealPolitiX/python_tutorial_FHI-PC-SESD/blob/master/materials/PyTutorial_03_Numerics.ipynb)
1. [numpy](http://www.numpy.org/) (matrix calculation)
2. [scipy](https://www.scipy.org/) (numerical methods, signal processing)
3. [pandas](http://pandas.pydata.org/) (time series, panel data) 
4. [sympy](http://www.sympy.org) (symbolic calculation)
5. [mpmath](http://mpmath.org/) (arbitrary-precision calculation)


### 4. Python visualization & interactivity [:arrow_forward:](https://github.com/RealPolitiX/python_tutorial_FHI-PC-SESD/blob/master/materials/PyTutorial_04_Visualization.ipynb)
1. [matplotlib](https://matplotlib.org/) (2D) 
2. [seaborn](https://seaborn.pydata.org/) (2D stats) 
3. [mayavi](http://code.enthought.com/projects/mayavi/#Mayavi) (3D) 
4. [ipywidgets](https://github.com/jupyter-widgets/ipywidgets)/[bokeh](http://bokeh.pydata.org/)/[plotly](https://plot.ly/) (interactivity) 


### 5. Advanced python [:arrow_forward:](https://github.com/RealPolitiX/python_tutorial_FHI-PC-SESD/blob/master/materials/PyTutorial_05_AdvancedTopics.ipynb)
1. [PyQt](https://riverbankcomputing.com/software/pyqt/intro) (GUI incl. DaX interface) 
2. code profiling in Jupyter and using [line_profiler](https://github.com/rkern/line_profiler)
3. multiprocessing [py2](https://pymotw.com/2/multiprocessing/basics.html) | [py3](https://pymotw.com/3/multiprocessing/basics.html) (parallel computation)
4. [cython](http://cython.org/) (compiled python)
5. python 2.7 vs python 3.5 ([short summary](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html))
6. interfacing w/ other languages (Matlab/Julia/C(++)/Fortran)


### 6. Custom python packages for experimental analysis [:arrow_forward:](https://github.com/RealPolitiX/python_tutorial_FHI-PC-SESD/blob/master/materials/PyTutorial_06_NichePackages.ipynb)
1. [xarray](http://xarray.pydata.org) (nD array) 
2. [lmfit](https://lmfit.github.io/lmfit-py/)/[mystic](http://trac.mystic.cacr.caltech.edu)/[cvxpy](http://www.cvxpy.org) (nonlinear regression, convex optimization) 
3. [deap](https://github.com/DEAP/deap) (evolutionary algorithm) 
4. [scikit-image](http://scikit-image.org/) (image analysis) 
5. [scikit-learn](http://scikit-learn.org) (machine learning) 
6. [pyFAI](https://github.com/silx-kit/pyFAI) (fast radial integrator)
7. [larch](http://cars9.uchicago.edu/xraylarch/) (XAFS)
8. [diffpy](http://www.diffpy.org/) (diffraction) 
9. [mpes](https://github.com/RealPolitiX/mpes)
