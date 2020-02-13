# TFGP

A Python Genetic Programming package for biinary classification and regression that uses tensorflow for faster performance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Requires python3

Tensorflow: Any version from 1.4 untill 2.x, before 2.x there is a need to declare eager execution, from 2.x onwards, that is done automaticaly.

Sckit-learn: Any of the latest versions

```
pip install tensorflow
pip install pandas
pip install sklearn
pip install multiprocessing
pip install pickle
```

## Modules

A brief explanation 



### Data Processing

```
DataHandler
```
This file loads and preprocesses(if defined) the dataset being used.

### Genetic Operators
```
GeneticOperators
```
This file contains the implementation of both crossover and mutation operators.

### Population Operations
```
Tree
Forest
Selection
ReproductionHandler
```


### Utility
```
Utils
SavingHandler
excelScript
```
Utils contains the implementations of protected operations and math fucntions with multiple applications.

SavingHandler contains the functions used to data.

excelScript is a simple script used to merge all csvs in a folder into a single one, uses include joining the individual results from runs for easier visualization and analysis.


## Datasets

This folder contains datasets that can be used to test this package.
```
Breast Cancer Wisconsin
GAMETES
Heart
Ionosphere
Parkinsons
Sonar
```



## **How to use**

The main file is th **GP.py** file. This is the file used to run the algorithm as it contains the evolutionary cycle.


### **Parameter List**
Parameters | Description
-----------|------------
csvname | name of the dataset to use
dsetpath | path to the dataset folder
forest_type | Can be ramped_forest, full_forest or grow_forest
fpath | path to the individuals folder
loadname | name of the population to load
ngens | number of generations
nruns | number of runs
popsize | population size, the number of individuals
resume | False to start a fresh run, True to laod a population and start from there (Future Work)
savename | name to save the population from the last complete generation
savesheetdir | path to the folder containing the resulting csv files
sheetname | name of the reasulting csv file with training and testing values from each generation
tsize | standard tournament size
ttype | tournament type, 1 is standard, 2 is double



### **Parameter List (Tree)**
Parameters | Description
-----------|------------
biFunctions | list of binary functions that can be used
uniFunctions | list of unary functions that can be used
maxDepth | maximum depth of the first generated trees (root starts at 0)


### **Parameter List (Reproduction)**
Parameters | Description
-----------|------------
MUTATIONPERCENT | percentage of the mutation operator
CROSSOVERPERCENT | percentage of the crossover operator

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
