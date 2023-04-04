# README

This repository is a workflow manager for an SU(4) baryon-baryon scattering project.  This program takes as input a list of operators, performs the wick contractions, and outputs a list of diagrams.   

The best place to get started is to look at the *uuuu_baryon* ipython notebook, which includes notes and an example running through all of the code from start to end.  Before doing this you need to install the [WickContractions library](github.com/chrisculver/WickContractions).

Evaluation of the diagrams is performed by the *baryons* branch of [lapH_build_and_run](https://gitlab.com/Kimmy.Cushman/laph_build_and_run).

## TODO

* Interface with operator construction library
* Better integration with [ContractionOptimizer](https://github.com/laphnn/contraction_optimizer)
* Store wick contraction results in a database instead of computing them
* Correlation matrix management (should probably just copy [CMM](github.com/chrisculver/CorrelationMatrixManager) for mesons
* Operator Management
    * Isospin combinations 
    * Momentum (just replace x with p?)
    * Displacements?