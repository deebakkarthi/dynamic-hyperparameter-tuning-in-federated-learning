#!/usr/bin/env python3
from ConfigSpace import Configuration, ConfigurationSpace

import numpy as np
from smac import HyperparameterOptimizationFacade, Scenario
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

X, y= datasets.load_iris(return_X_y=True)


def train(config: Configuration, seed: int = 0) -> float:
    classifier = SVC(C=config["C"], random_state=seed)
    scores = cross_val_score(classifier, X, y, cv=5)
    return 1 - np.mean(scores)


configspace = ConfigurationSpace({"C": (0.100, 1000.0)})

# Scenario object specifying the optimization environment
scenario = Scenario(configspace, deterministic=True, n_trials=200)

# Use SMAC to find the best configuration/hyperparameters
smac = HyperparameterOptimizationFacade(scenario, train)
incumbent = smac.optimize()
print(incumbent)
