import random
import csv
import numpy as np
import time
import matplotlib.pyplot as plt
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

def main(pop_size=300, mutation_prob=0.2, tournament_size=3):

    toolbox.register(
        "select",
        tools.selTournament,
        tournsize=tournament_size
    )

    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)  # Hall of Fame to store the best individual

    # Setup statistics to track
    stats = tools.Statistics(lambda ind: ind.fitness.values)

    stats.register(
        "avg_distance",
        lambda fits: np.mean([f[0] for f in fits])
    )

    stats.register(
        "avg_imbalance",
        lambda fits: np.mean([f[1] for f in fits])
    )

    stats.register(
        "min_distance",
        lambda fits: np.min([f[0] for f in fits])
    )

    stats.register(
        "min_imbalance",
        lambda fits: np.min([f[1] for f in fits])
    )

    # Run the genetic algorithm
    pop ,logbook =   algorithms.eaSimple(
        pop,
        toolbox,
        0.7,
        mutation_prob,
        30,
        stats=stats,
        halloffame=hof
        )
    return pop, logbook, hof

def run_experiment(pop_size, mutation_prob, tournament_size):
    start_time = time.time()

    pop, logbook, hof = main(
        pop_size=pop_size,
        mutation_prob=mutation_prob,
        tournament_size=tournament_size
    )

    end_time = time.time()

    best = hof[0]

    total_distance = best.fitness.values[0]
    imbalance = best.fitness.values[1]
    runtime = end_time - start_time

    return total_distance, imbalance, runtime

def convergence_analysis():
    pop, logbook, hof = main(
        pop_size=300,
        mutation_prob=0.2,
        tournament_size=3
    )

    results = []

    for record in logbook:
        results.append([
            record["gen"],
            record["avg_distance"],
            record["min_distance"],
            record["avg_imbalance"],
            record["min_imbalance"]
        ])

    save_convergence_results(results)

    print("Convergence analysis completed.")
    print("Results saved to convergence_analysis.csv")

def save_results(results):
    with open("parameter_tuning.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "experiment",
            "population_size",
            "mutation_probability",
            "tournament_size",
            "total_distance",
            "imbalance",
            "runtime"
        ])

        writer.writerows(results)

def save_convergence_results(results):
    with open("convergence_analysis.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "generation",
            "avg_distance",
            "min_distance",
            "avg_imbalance",
            "min_imbalance"
        ])

        writer.writerows(results)

def plot_convergence():
    data = np.genfromtxt(
        "convergence_analysis.csv",
        delimiter=",",
        names=True
    )

    generations = data["generation"]

    # Distance convergence
    plt.figure()
    plt.plot(
        generations,
        data["avg_distance"],
        label="Average Distance"
    )
    plt.plot(
        generations,
        data["min_distance"],
        label="Minimum Distance"
    )
    plt.xlabel("Generation")
    plt.ylabel("Distance")
    plt.title("Distance Convergence")
    plt.legend()
    plt.show()

    # Imbalance convergence
    plt.figure()
    plt.plot(
        generations,
        data["avg_imbalance"],
        label="Average Imbalance"
    )
    plt.plot(
        generations,
        data["min_imbalance"],
        label="Minimum Imbalance"
    )
    plt.xlabel("Generation")
    plt.ylabel("Route Imbalance")
    plt.title("Route Imbalance Convergence")
    plt.legend()
    plt.show()

def parameter_tuning():
    results = []

    population_sizes = [100, 300, 500]

    for size in population_sizes:
        distance, imbalance, runtime = run_experiment(
            pop_size=size,
            mutation_prob=0.2,
            tournament_size=3
        )

        results.append([
            "population_size",
            size,
            0.2,
            3,
            distance,
            imbalance,
            runtime
        ])

    mutation_probabilities = [0.1, 0.2, 0.4]

    for mutation in mutation_probabilities:
        distance, imbalance, runtime = run_experiment(
            pop_size=300,
            mutation_prob=mutation,
            tournament_size=3
        )

        results.append([
            "mutation_probability",
            300,
            mutation,
            3,
            distance,
            imbalance,
            runtime
        ])

    tournament_sizes = [2, 3, 5]

    for tournament in tournament_sizes:
        distance, imbalance, runtime = run_experiment(
            pop_size=300,
            mutation_prob=0.2,
            tournament_size=tournament
        )

        results.append([
            "tournament_size",
            300,
            0.2,
            tournament,
            distance,
            imbalance,
            runtime
        ])

    save_results(results)
    print("Parameter tuning completed.")
    print("Results saved to parameter_tuning.csv")

# if __name__ == "__main__":
#     parameter_tuning()

if __name__ == "__main__":
    convergence_analysis()
    plot_convergence()