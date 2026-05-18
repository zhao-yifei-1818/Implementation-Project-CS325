import time
import random
import ast

"""
Take an array of numbers and find the subarray
whose sum is closest to 0.
"""


def read_arrays_from_file(filename):
    arrays = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line:  # skip empty lines
                arr = ast.literal_eval(line)
                arrays.append(arr)

    return arrays
def gen_array(size):
    arr = []

    for i in range(size):
        num = random.randint(-100, 100)
        arr.append(num)

    return arr


def betterEnumeration(arr):
    best_sum = float("inf")
    best_subarray = []

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum += arr[j]

            # keep best sum closest to 0
            if abs(current_sum) < abs(best_sum):
                best_sum = current_sum
                best_subarray = arr[i:j + 1]

    return abs(best_sum), best_subarray


if __name__ == "__main__":

    # 100,200,...,900
    for size in range(100, 1000, 100):

        clock_start = time.time()

        for i in range(10):
            arr = gen_array(size)
            betterEnumeration(arr)

        clock_end = time.time()

        average_time = (clock_end - clock_start) / 10

        print(size, average_time)


    # 1000,2000,...,9000
    for size in range(1000, 10000, 1000):

        clock_start = time.time()

        for i in range(10):
            arr = gen_array(size)
            betterEnumeration(arr)

        clock_end = time.time()

        average_time = (clock_end - clock_start) / 10

        print(average_time)