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


def closest_to_zero(arr):
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

    arrays = read_arrays_from_file("test.txt")

    for index, arr in enumerate(arrays):

        best_sum, best_subarray = closest_to_zero(arr)

        print(f"Test Case {index + 1}")
        print("Closest sum to 0:", best_sum)
        print("Subarray:", best_subarray)
        print()