import sys
import time
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np


# 1)
def sequence_calculator(n: int) -> int:
    """
    find the nth number in sequence S_n = 3*S_(n-1) - S_(n-2), with S_0 = 0 and S_1 = 1
    :param n: nth number in the sequence, assuming n >= 0
    :return: the number of the nth number in the sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    n_minus_2 = 0
    n_minus_1 = 1
    ret = 0

    for i in range(2, n + 1):
        ret = 3 * n_minus_1 - n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = ret

    return ret


# 2)
# The time complexity for sequence_calculator is O(n). In this method, I use a dynamic programming technique to
# iteratively compute the sequence from index 0 to n. I use 2 variables to store the previous elements and one
# variable to store the current result. I loop through the indices from 0 to n, and inside the loop, I perform
# 3 constant-time operations, each of which takes O(1) time. Therefore, the overall time complexity for this method
# is O(n) since we perform O(1) work in each iteration of the loop.
#
# Side note: If I know that this method is going to be called frequently, I would store the results in a table
# (like a cache). This way, when multiple people access the method for different values of n, they could benefit
# from results that have already been calculated. In the best-case scenario, the overall time complexity with caching
# would approach O(1), with a sacrifice of space complexity being O(n). But here I did not use memoization for the
# purpose of justifying O(n) time complexity.


# 3)
def plot_execution_time(n: int = 100000) -> None:
    """
    plot the execution time from calculating the 1st number in the sequence, to the nth number in the sequence
    :param n: maximum number of sequence to calculate
    """
    counts, times = [], []
    for i in range(n):
        start_time = time.time()
        sequence_calculator(i)
        end_time = time.time()
        counts.append(i)
        times.append((end_time - start_time) / 1000)
    plt.figure()
    plt.clf()
    plt.plot(counts, times, label="Execution Time vs n")
    plt.xlabel('nth calculation')
    plt.ylabel('Time (milliseconds)')
    plt.title('sequence_calculator execution time vs sequence calculated')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('output/sequence_calculator_time.png')
    linear_fit(counts, times)


# 4)
# from my local run, the R^2 score is 85.81%, which justifies that the runtime vs number of n is a linear relation
def linear_fit(counts: list, times: list) -> None:
    """
    calculate the R^2 based on linear regression model, and save the result to output
    :param counts: list of nth number in the sequence (x)
    :param times:  list of runtime in milliseconds (y)
    """
    counts = np.array(counts).reshape(-1, 1)
    times = np.array(times)
    model = LinearRegression()
    model.fit(counts, times)
    predicted = model.predict(counts)
    r2 = r2_score(times, predicted)
    res = f'linear regression r2 of the execution time vs nth sequence: {r2 * 100}%'
    print(res)
    with open('output/r2_score.txt', 'w') as file:
        file.write(res)


def main() -> None:
    """
    entry point to sequence
    """
    sys.set_int_max_str_digits(100000)
    print(sequence_calculator(100000))
    plot_execution_time()
