from asyncio.windows_events import NULL
import utilities as util

def tabou(solution, customers, vehicle_capacity, distances, max_iterations = 20, number_neighbors = 5):
    best_solution = solution.copy()
    current_solution = solution.copy()

    iteration = 0
    visited_solutions = []
    best_solution_index = 0

    graph = []

    while iteration - best_solution_index < max_iterations :
        neighborhood = util.generate_neighborhood(current_solution, customers, vehicle_capacity, switchNodes=number_neighbors)

        best_neighbor = neighborhood[0]
        for neighbor in neighborhood[1:]:
            if not (neighbor in visited_solutions):
                if util.cost_function(neighbor, distances) < util.cost_function(best_neighbor, distances):
                    best_neighbor = neighbor
        
        visited_solutions.append(best_neighbor)

        current_solution = best_neighbor.copy()

        if util.cost_function(current_solution, distances) < util.cost_function(best_solution, distances):
            best_solution = current_solution.copy()
            best_solution_index = iteration

        graph.append(util.cost_function(current_solution, distances))
        iteration += 1

    return best_solution, graph

