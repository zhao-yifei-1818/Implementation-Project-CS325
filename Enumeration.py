import ast

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

    arrays = read_arrays_from_file("test.txt")

    for index, arr in enumerate(arrays):

        best_sum, best_subarray = enumeration(arr)

        print(f"Test Case {index + 1}")
        print("Closest sum to 0:", best_sum)
        print("Subarray:", best_subarray)
        print()