import numpy as np
import matplotlib.pyplot as plt



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

def plot_diversity():

    data = np.genfromtxt(
        "diversity_analysis.csv",
        delimiter=",",
        names=True
    )

    plt.figure()

    plt.plot(
        data["generation"],
        data["average_diversity"],
        marker="o"
    )

    plt.xlabel("Generation")
    plt.ylabel("Average Diversity")
    plt.title("Solution Diversity Over Generations")
    plt.grid(True)

    plt.show()