#!/usr/bin/env python

from ConfigSpace import Configuration, ConfigurationSpace

from smac import HyperparameterOptimizationFacade, Scenario


# Simple quadratic function to optimize
def f(config: Configuration, seed: int = 0):
    return config["x"] ** 2


configspace = ConfigurationSpace({"x": (-10e5, 10e5)})


scenario = Scenario(configspace, deterministic=True, n_trials=200)


smac = HyperparameterOptimizationFacade(scenario, f)

incumbent = smac.optimize()

print(incumbent)
