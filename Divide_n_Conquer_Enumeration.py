import random
import ast


def read_arrays_from_file(filename):
    arrays = []

    with open(filename, "r") as file:
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


def get_size():
    size = int(input("Enter array size: "))
    return size


def solve(arr, start, end):

    # base case 1 element
    if start == end:
        return (arr[start], start, end)
    # divide by 2
    mid = (start + end) // 2

    # Recursive
    left_result = solve(arr, start, mid)
    right_result = solve(arr, mid + 1, end)

    # Enumeration,theta n^2

    # placeholder for cross_result(sum,start,end)
    best_cross_sum = float("inf")
    best_cross_start = 0
    best_cross_end = 0
    left_sum = 0
    # walk backward from mid to left

    for i in range(mid, start - 1, -1):
        # every combination of:
        left_sum += arr[i]  # get the left index total
        right_sum = (
            0  # when i move left, recalculate, do this by set it to 0 every time
        )
        for j in range(mid + 1, end + 1):
            right_sum += arr[j]
            total = left_sum + right_sum
            # if any total found is better than infinity or what we have
            if abs(total) < abs(best_cross_sum):
                # record its sum and indexes if it's a better one
                best_cross_sum = total
                best_cross_start = i
                best_cross_end = j

    cross_result = (
        # this is enumeration result at the end
        best_cross_sum,
        best_cross_start,
        best_cross_end,
    )

    # compare:
    best_result = left_result
    if abs(right_result[0]) < abs(best_result[0]):
        best_result = right_result
    if abs(cross_result[0]) < abs(best_result[0]):
        best_result = cross_result

    # return (sum,start,end)
    return best_result


def close_to_zero(arr):
    if len(arr) == 0:
        return None
    best_sum, start, end = solve(arr, 0, len(arr) - 1)
    return best_sum, arr[start : end + 1]


if __name__ == "__main__":

    # size = get_size()

    # A = gen_array(size)

    A = read_arrays_from_file("test.txt")

    for index, arr in enumerate(A):

        best_sum, best_subarray = close_to_zero(arr)

        print(f"Test Case {index + 1}")
        print("Closest sum to 0:", best_sum)
        print("Subarray:", best_subarray)
        print()
