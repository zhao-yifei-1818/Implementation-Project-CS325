import time
import random
import ast
def gen_array(size):
    arr = []

    for i in range(size):
        num = random.randint(-100, 100)
        arr.append(num)

    return arr
def read_arrays_from_file(filename):

    arrays = []

    with open(filename, "r") as file:

        for line in file:

            line = line.strip()

            if line:

                arr = ast.literal_eval(line)
                arrays.append(arr)

    return arrays


def enumeration(arr):

    best_sum = float("inf")

    best_i = 0
    best_j = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            if abs(current_sum) < abs(best_sum):
                best_sum = current_sum
                best_i = i
                best_j = j

    best_subarray = arr[best_i:best_j + 1]

    return abs(best_sum), best_subarray


if __name__ == "__main__":

    for size in range (100,1000,100):
        clock_start = time.time()
        for size2 in range (1,10,1):
            enumeration(gen_array(size))
            clock_end = time.time()
        print(clock_end-clock_start)