# Vehicle Routing Optimization using Genetic Algorithms

A Python implementation of the Vehicle Routing Problem (VRP) using Genetic Algorithms and the DEAP library.

## About the Project

The Vehicle Routing Problem is an optimization problem where multiple vehicles need to visit a set of locations while starting and ending at a common depot.

This project uses a Genetic Algorithm to find efficient routes for multiple vehicles.

## Features

- Generates random locations and a depot
- Uses Genetic Algorithms to optimize vehicle routes
- Minimizes total travel distance
- Considers balance between vehicle route distances
- Uses DEAP for evolutionary computation
- Visualizes routes using Matplotlib

## Technologies Used

- Python
- DEAP
- NumPy
- Matplotlib

## Genetic Algorithm

The project uses:

- Population of candidate routes
- Tournament selection
- Partially Matched Crossover (PMX)
- Shuffle Index Mutation
- Multi-objective fitness evaluation

## Current Status

Basic Vehicle Routing Problem implementation completed.

Further experiments and analysis will be added to study the effect of genetic algorithm parameters and solution behavior.