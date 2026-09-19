# Vehicle Routing Optimization using Genetic Algorithms

A Python-based implementation of the **Vehicle Routing Problem (VRP)** using a **Genetic Algorithm (GA)** and the **DEAP** evolutionary computation framework.

The project not only finds optimized vehicle routes but also analyzes how Genetic Algorithm parameters, convergence, and population diversity affect the optimization process.

---

## 📌 About the Project

The **Vehicle Routing Problem (VRP)** is a classic optimization problem where multiple vehicles must visit a set of locations while starting and ending at a common depot.

The objective is to find efficient routes while considering:

* Total travel distance
* Balance between vehicle route distances
* Evolution of candidate solutions across generations

This project uses a **permutation-based Genetic Algorithm** to generate and evolve possible routing solutions.

---

## 🎯 Project Objectives

The project was developed to:

* Implement a Genetic Algorithm for a Vehicle Routing Problem
* Optimize total vehicle travel distance
* Maintain better balance between vehicle routes
* Study the effect of Genetic Algorithm parameters
* Analyze solution convergence across generations
* Analyze population diversity during evolution
* Visualize and interpret the behavior of the optimization process

---

## ✨ Features

### 1. Vehicle Routing Problem

* Generates random locations using `(x, y)` coordinates
* Uses a fixed depot
* Supports multiple vehicles
* Represents each solution as a permutation of locations
* Calculates the total distance travelled by all vehicles
* Calculates route imbalance using standard deviation

### 2. Genetic Algorithm Optimization

The project uses:

* **Population-based evolutionary search**
* **Tournament Selection**
* **Partially Matched Crossover (PMX)**
* **Shuffle Index Mutation**
* **Multi-objective fitness function**
* **Hall of Fame** to retain the best solution found

The fitness function minimizes:

1. Total travel distance
2. Route imbalance between vehicles

### 3. Parameter Tuning

The effect of important Genetic Algorithm parameters was experimentally evaluated.

| Parameter            | Values Tested |
| -------------------- | ------------- |
| Population Size      | 100, 300, 500 |
| Mutation Probability | 0.1, 0.2, 0.4 |
| Tournament Size      | 2, 3, 5       |

A **one-factor-at-a-time (OFAT)** approach was used so that the effect of each parameter could be examined while keeping the other parameters fixed.

For each experiment, the following were recorded:

* Total distance
* Route imbalance
* Runtime

Results are stored in:

```text
parameter_tuning.csv
```

### 4. Convergence Analysis

The project tracks how the fitness metrics change over generations.

The following metrics are recorded:

* Average distance
* Minimum distance
* Average route imbalance
* Minimum route imbalance

Results are stored in:

```text
convergence_analysis.csv
```

This helps analyze how the Genetic Algorithm's objective values change throughout the evolutionary process.

### 5. Solution Diversity Analysis

The project measures how different the candidate solutions are from one another during evolution.

Since each solution is represented as a permutation, **Hamming distance** is used to measure the difference between two candidate solutions.

The average pairwise Hamming distance of the population is calculated for every generation.

Results are stored in:

```text
diversity_analysis.csv
```

This helps analyze how the similarity between candidate solutions changes as the Genetic Algorithm evolves.

---

## 📊 Results & Analysis

### 1. Convergence Analysis

The convergence analysis visualizes how distance and route imbalance change over generations.

![Convergence Analysis](assets/convergence_analysis.png)

The graph helps observe how the optimization metrics change and begin to stabilize as the Genetic Algorithm evolves.

---

### 2. Solution Diversity Analysis

The diversity analysis shows how the average difference between candidate solutions changes over generations.

![Solution Diversity Analysis](assets/diversity_analysis.png)

In the current experiment, population diversity decreases substantially over generations. This indicates that candidate solutions become increasingly similar as the Genetic Algorithm evolves.


## 🧬 Genetic Algorithm Workflow

```text
Generate Locations
        ↓
Generate Initial Population
        ↓
Evaluate Fitness
        ↓
Tournament Selection
        ↓
PMX Crossover
        ↓
Shuffle Mutation
        ↓
Evaluate New Population
        ↓
Repeat for Multiple Generations
        ↓
Store Best Solution
        ↓
Analyze Convergence & Diversity
```

---

## 🧠 Key Concepts Demonstrated

This project provides practical exposure to:

* Genetic Algorithms
* Evolutionary Computation
* Vehicle Routing Problem
* Permutation-based representations
* Multi-objective optimization
* Tournament Selection
* PMX Crossover
* Mutation
* Fitness Functions
* Population Diversity
* Convergence Analysis
* Parameter Tuning
* Data Analysis using NumPy
* Data Visualization using Matplotlib

---

## 🛠️ Technologies Used

* **Python**
* **DEAP** – evolutionary computation and Genetic Algorithms
* **NumPy** – numerical calculations and statistical analysis
* **Matplotlib** – data visualization
* **CSV** – storing experimental results

---

## 📂 Project Structure

```text
vehicle-routing-genetic-algorithm/
│
├── main.py
├── vrp.py
├── analysis.py
├── visualization.py
│
├── parameter_tuning.csv
├── convergence_analysis.csv
├── diversity_analysis.csv
│
├── assets/
│   ├── convergence_analysis.png
│   └── diversity_analysis.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

### File Responsibilities

| File                       | Purpose                                              |
| -------------------------- | ---------------------------------------------------- |
| `main.py`                  | Runs the selected analyses                           |
| `vrp.py`                   | Core VRP and Genetic Algorithm implementation        |
| `analysis.py`              | Parameter tuning, convergence and diversity analysis |
| `visualization.py`         | Generates analysis plots                             |
| `parameter_tuning.csv`     | Parameter experiment results                         |
| `convergence_analysis.csv` | Generation-wise convergence results                  |
| `diversity_analysis.csv`   | Generation-wise diversity results                    |
| `requirements.txt`         | Python dependencies                                  |

---

## ⚙️ Installation

Clone the repository and navigate into the project directory.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run:

```bash
python main.py
```

The main script runs the currently selected analysis and generates its corresponding visualization.
---

## 📈 Experimental Analysis

The project goes beyond simply finding a routing solution.

Three experiments were implemented:

### Parameter Tuning

Studies how changes in:

* Population size
* Mutation probability
* Tournament size

affect the Genetic Algorithm.

### Convergence Analysis

Studies how the population's fitness values change across generations.

### Diversity Analysis

Studies how the similarity between candidate solutions changes throughout the evolutionary process.

Together, these experiments provide insight into both the **performance** and **behavior** of the Genetic Algorithm.

---

## 🚀 Future Improvements

Possible extensions include:

* Larger and more realistic datasets
* Real-world geographic coordinates
* Vehicle capacity constraints
* Time-window constraints
* Dynamic routing scenarios
* Comparison with other optimization algorithms
* Interactive route visualization
* More extensive parameter experiments

---

## 📌 Current Status

### Completed

* [x] Vehicle Routing Problem implementation
* [x] Genetic Algorithm optimization
* [x] Multi-objective fitness evaluation
* [x] Parameter tuning
* [x] Convergence analysis
* [x] Solution diversity analysis
* [x] Experimental result storage
* [x] Data visualization
* [x] Modular project structure

---

## 👩‍💻 Author

**Aarushi**

A learning-focused project exploring Genetic Algorithms, optimization, and data analysis using Python.
