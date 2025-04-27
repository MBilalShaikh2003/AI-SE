import operator
import math
import random
import numpy as np
from deap import algorithms, base, creator, tools, gp

# Define the target function
def target_function(x):
    return 5*x**3 - 6*x**2 + 8*x

# Create the primitive set
def create_primitive_set():
    pset = gp.PrimitiveSet("MAIN", 1)  # 1 input variable (X)
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(math.sin, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
    pset.renameArguments(ARG0='x')
    return pset

# Evaluation function (using RMSE)
def evaluate(individual, points, toolbox):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    
    # Evaluate the mean squared error between the expression and the target function
    sqerrors = []
    for x in points:
        try:
            pred = func(x)
            true_val = target_function(x)
            sqerrors.append((pred - true_val)**2)
        except (OverflowError, ValueError):
            return 10000,  # Return a large error for invalid results
    
    if not sqerrors:  # All evaluations failed
        return 10000,
    
    rmse = math.sqrt(sum(sqerrors)/len(sqerrors))
    return rmse,

# Create the toolbox
def create_toolbox(pset):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)
    
    toolbox = base.Toolbox()
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)
    
    # Evaluation function with 20 random points between -1 and 1
    points = [random.uniform(-1, 1) for _ in range(20)]
    toolbox.register("evaluate", lambda ind: evaluate(ind, points, toolbox))
    
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
    
    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    
    return toolbox

def main():
    random.seed(42)
    
    pset = create_primitive_set()
    toolbox = create_toolbox(pset)
    
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("std", np.std)
    mstats.register("min", np.min)
    mstats.register("max", np.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats, 
                                  halloffame=hof, verbose=True)
    
    # Print the best individual
    best_ind = hof[0]
    print("\nBest individual:")
    print(best_ind)
    print(f"Expression: {str(best_ind)}")
    
    # Test the best individual
    func = toolbox.compile(expr=best_ind)
    test_points = [0.1, 0.5, 1.0, -0.5, -1.0]
    print("\nTesting best individual:")
    for x in test_points:
        try:
            pred = func(x)
            true_val = target_function(x)
            error = abs(pred - true_val)
            print(f"x={x:.2f}: Predicted={pred:.2f}, True={true_val:.2f}, Error={error:.2f}")
        except (OverflowError, ValueError):
            print(f"x={x:.2f}: Evaluation failed")

if __name__ == "__main__":
    main()