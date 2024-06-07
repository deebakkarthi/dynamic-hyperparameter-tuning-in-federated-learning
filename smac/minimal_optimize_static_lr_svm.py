#!/usr/bin/env python

from gc import callbacks

import numpy as np
from ConfigSpace import Categorical, Configuration, ConfigurationSpace, Float, Integer
from ConfigSpace.conditions import InCondition
from sklearn import datasets, svm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import max_error
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from smac import Callback, HyperparameterOptimizationFacade, Scenario

X, y = datasets.load_breast_cancer(return_X_y=True)


def train(config: Configuration, seed: int = 0) -> float:
    classifier = make_pipeline(
        StandardScaler(), SGDClassifier(learning_rate="constant", **config)
    )
    scores = cross_val_score(classifier, X, y, cv=10)
    cost = 1 - np.mean(scores)
    print(f"LR={config['eta0']}, COST={cost}")
    return cost


if __name__ == "__main__":
    configspace = ConfigurationSpace({"eta0": Float("eta0", (0, 1))})
    stop_after = 10
    scenario = Scenario(
        configspace,
        n_trials=200,
    )
    initial_design = HyperparameterOptimizationFacade.get_initial_design(
        scenario, n_configs=5
    )
    smac = HyperparameterOptimizationFacade(scenario, train, overwrite=True)
    incumbent = smac.optimize()

    default_cost = smac.validate(configspace.get_default_configuration())
    print(f"Default cost: {default_cost}")

    incumbent_cost = smac.validate(incumbent)  # type: ignore
    print(f"Incumbent={incumbent}, Incumbent cost: {incumbent_cost}")
