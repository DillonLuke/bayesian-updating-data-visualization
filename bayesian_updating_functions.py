import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

def get_binom_post_dist(parameters, priors, k: int, n: int):
    likelihoods = np.array([binom.pmf(k, n, param) for param in parameters])
    
    likelihoods_x_priors = likelihoods * priors
    
    posterior_probabilities = likelihoods_x_priors / likelihoods_x_priors.sum()
    
    return posterior_probabilities


def format_results(post_dist_array, num_exp: int, parameters):
    experiment_number_array = np.repeat(range(1, num_exp+1), len(parameters))
    
    parameter_array = np.tile(parameters, num_exp)
    
    results = pd.DataFrame({"Experiment_Number": experiment_number_array,
                            "Parameter": parameter_array, 
                            "Posterior_Probability": np.ravel(post_dist_array)})
    
    return results


def coin_toss_simulation(num_exp: int, n: int, p: float, parameters, initial_priors):
    posterior_distributions = []
    
    current_prior = initial_priors
    for i in range(num_exp):
        current_k = binom.rvs(n, p, random_state=np.random.randint(1, 1000))
        
        posterior_distributions.append(get_binom_post_dist(parameters,
                                                           current_prior,
                                                           current_k,
                                                           n))
        
        current_prior = posterior_distributions[-1]
    
    
    return format_results(posterior_distributions, num_exp, parameters)


def display_results(simulation_results: pd.DataFrame):
    num_exp = simulation_results["Experiment_Number"].nunique()
    
    lp = sns.lineplot(data=simulation_results,
                      x="Parameter",
                      y="Posterior_Probability",
                      hue="Experiment_Number",
                      palette=sns.color_palette("Greys", num_exp));
    
    handles, labels = lp.get_legend_handles_labels()
    
    step = max(1, int(num_exp//10)) # step to get only 10 handles/labels
                
    lp.legend(handles[::step], labels[::step], title="Experiment Number")
