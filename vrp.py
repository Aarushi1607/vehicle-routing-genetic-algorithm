import random
import numpy as np
from deap import creator, base, tools ,algorithms

random.seed(42)
num_locations = 10
locations = [(random.randint(0, 100), random.randint(0, 100))
             for _ in range(num_locations)]# ggenerates 10 random (x,y) coordinates
depot = (50,50)
num_vehicles = 3

creator.create("FitnessMin", base.Fitness, weights=(-1.0,-1.0,))
creator.create("Individual", list ,fitness=creator.FitnessMin)

toolbox=base.Toolbox()
toolbox.register("indices", random.sample, range(num_locations), num_locations)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population",tools.initRepeat, list, toolbox.individual)

def evalvrp(individual):
    td=0
    distances=[]

    for i in range(num_vehicles):
        vehicle_route = [depot] + [locations[individual[j]]
            for j in range(i, len(individual), num_vehicles)] + [depot]#range(0,10,3)

        vehicle_distance = sum(
            np.linalg.norm(
                np.array(vehicle_route[k+1]) -
                np.array(vehicle_route[k])
            )
            for k in range(len(vehicle_route)-1)
        )

        td += vehicle_distance
        distances.append(vehicle_distance)

    std_dev = np.std(distances)

    return (td, std_dev)

  

toolbox.register("evaluate",evalvrp)
toolbox.register("select",tools.selTournament,tournsize=3)
toolbox.register("mate",tools.cxPartialyMatched )
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)


def main(pop_size=300, mutation_prob=0.2, tournament_size=3,track_population=False):

    toolbox.register(
        "select",
        tools.selTournament,
        tournsize=tournament_size
    )

    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)  # Hall of Fame to store the best individual

    # Setup statistics to track
    stats = tools.Statistics(lambda ind: ind )

    stats.register(
    "avg_distance",
    lambda individuals: np.mean(
        [ind.fitness.values[0] for ind in individuals]
    )
    )

    stats.register(
    "avg_imbalance",
    lambda individuals: np.mean(
        [ind.fitness.values[1] for ind in individuals]
    )
)

    stats.register(
    "min_distance",
    lambda individuals: np.min(
        [ind.fitness.values[0] for ind in individuals]
    )
)

    stats.register(
    "min_imbalance",
    lambda individuals: np.min(
        [ind.fitness.values[1] for ind in individuals]
    )
)

    if track_population:
        stats.register(
            "population",
            lambda individuals: [list(ind) for ind in individuals]
        )

    # Run the genetic algorithm
    pop ,logbook =   algorithms.eaSimple(
        pop,
        toolbox,
        0.7,
        mutation_prob,
        30,
        stats=stats,
        halloffame=hof,
        verbose=not track_population
        )
    return pop, logbook, hof