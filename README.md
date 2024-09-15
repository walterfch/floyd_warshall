# README #

Please complete this document

### What is this repository for? ###
This is a python package that functions to recursively calculate a distance matrix by the Floyd-Warshall algorithm.
It is achieved by rewriting the iterative version of the algorithm at the "floyds/src/iterative" folder.
The package is written in accordance to PEP 8 guidelines.

### How do I get set up? ###
This package in written with Python 3.10 . 

To install this package use pip or pip3:

pip install git+https://github.com/walterfch/floyd_warshall.git


### Running the scripts ###
To run this package, please import it by:

from recursion.recursive_floyd_done import FW

Or, run it at your IDE or CLI (from the repository's root directory):

python3 recursion/recursive_floyd_done.py

The input of data to the script should be provided as the format below:

GRAPH = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

For the NO_PATH among the nodes, it is set to be:

from sys import maxsize

NO_PATH = maxsize

### Performance Tests ###
Performance tests run using  "process_time" from "time".
To access the performance tests, please run:

python3 tests/performance_test_done.py

### Unit Tests ###
To access the unit tests, please run:

python3 tests/unittests_done.py


### Requirements ### 
Please check the requirements.txt


