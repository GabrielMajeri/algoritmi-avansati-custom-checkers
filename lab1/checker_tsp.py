import io

from math import sqrt
from dmoj.result import CheckerResult

EPSILON = 0.5

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_cost(cycle):
    cost = 0
    for i in range(len(cycle)):
        cost += distance(cycle[i - 1], cycle[i])
    return cost

def check(process_output, judge_output, **kwargs):
    process_output = io.StringIO(process_output.decode('utf-8'))
    judge_output = io.StringIO(judge_output.decode('utf-8'))

    # Read the Hamiltonian cycle defined in the expected test output file.
    judge_output_lines = filter(lambda l: l != '', map(lambda l: l.strip(), judge_output))
    expected_cycle = [tuple(int(x) for x in line.split()) for line in judge_output]

    # Read the cycle the solution produced.
    process_output_lines = filter(lambda l: l != '', map(lambda l: l.strip(), process_output))
    cycle = [tuple(int(x) for x in line.split()) for line in process_output_lines]

    if len(expected_cycle) != len(cycle):
        return CheckerResult(False, 0, f"solution contains {len(cycle)} nodes, expected {len(expected_cycle)} nodes")

    expected_cost = total_cost(expected_cycle)
    cost = total_cost(cycle)
    if cost > expected_cost + EPSILON:
        return CheckerResult(False, 0, f"solution is longer than optimum: {cost:.2f} > {expected_cost:.2f}")

    if len(expected_cycle) != len(cycle):
        return CheckerResult(False, 0, "solution doesn't have right number of points")

    return True
