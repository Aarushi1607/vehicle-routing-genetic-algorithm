import csv
import time
import numpy as np

from vrp import main


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