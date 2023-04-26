# Bayesian Updating Data Visualization
The purpose of this project is to provide a visualization of Bayesian updating in the context of a coin toss experiment. 

In each experiment, a coin with some probability of heads (*p*) is flipped some number of times (*n*). After each experiment, the posterior probability of *p* for a range of possible values is updated using:
1. a prior probability distribution for each possible value of *p* 
2. the likelihood of the number of heads obtained over *n*, given each possible value of *p*

The experiment is repeated some number of times. The probability of heads, *p*, the number of coin tosses per experiment, *n*, and the number of experiments are defined by the user. The prior probability distribution for some range of possible *p* values is specified by the user for the first experiment; after the first experiment, the posterior probability for a given experiment will be used as the prior probability for the next experiment. The likelihood of obtaining some number of heads during a given experiment for each possible value of *p* is given by a binomial distribution (with parameters *p* and *n*). 

The data visualization workflow can be seen in **"Bayesian Updating Data Visualization.ipynb"**, which relies on custom functions found in **"bayesian_updating_functions.py."**