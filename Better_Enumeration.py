import time
import random
import ast

"""William Zhao
CS325 Implementation Project
Algorithm 2 Better Enumeration"""


def gen_array(size):
    arr = []

    for i in range(size):
        num = random.randint(-100, 100)
        arr.append(num)

    return arr


# Algorithm 2
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
                best_subarray = arr[i : j + 1]

    return abs(best_sum), best_subarray


if __name__ == "__main__":
    # time take for 100-900, average from 10 tries
    for size in range(100, 1000, 100):
        clock_start = time.perf_counter()
        for i in range(10):
            betterEnumeration(gen_array(size))
        clock_end = time.perf_counter()
        print((clock_end - clock_start) / 10)
    # time take for 1000-9000, average from 10 tries
    for size in range(1000, 10000, 1000):
        clock_start = time.perf_counter()
        for i in range(10):
            betterEnumeration(gen_array(size))
        clock_end = time.perf_counter()
        print((clock_end - clock_start) / 10)
