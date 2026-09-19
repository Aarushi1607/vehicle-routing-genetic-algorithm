import random
import numpy as np
import matplotlib.pyplot as plt
from deap import creator, base, tools ,algorithms

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

# Plotting Function
def plot_routes(individual, title="Routes"):
    plt.figure()
    # Plot locations as blue dots and the depot as a red square
    for (x, y) in locations:
        plt.plot(x, y, 'bo')
    plt.plot(depot[0], depot[1], 'rs')

    # Draw routes for each vehicle
    for i in range(num_vehicles):
        vehicle_route = [depot] + [locations[individual[j]] for j in range(i, len(individual), num_vehicles)] + [depot]
        plt.plot(*zip(*vehicle_route), '-')

    plt.title(title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

def main():
    random.seed(42)  # Seed for reproducibility
    pop = toolbox.population(n=300)  # Generate initial population
    hof = tools.HallOfFame(1)  # Hall of Fame to store the best individual

    # Setup statistics to track
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)

    # Run the genetic algorithm
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 300, stats=stats, halloffame=hof)
    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, hof = main()
    best = hof[0]
    print("Best route:", best)
    print("Total distance:", best.fitness.values[0])
    print("Route imbalance:", best.fitness.values[1])
    plot_routes(best, "Best VRP Solution")