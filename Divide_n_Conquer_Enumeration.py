import random
import ast
import time

"""William Zhao
CS325 Implementation Project
Algorithm 3 Divide and Conquer Enumeration"""


def gen_array(size):
    arr = []

    for i in range(size):
        num = random.randint(-100, 100)
        arr.append(num)

    return arr


def get_size():
    size = int(input("Enter array size: "))
    return size


# helper function that returns array
def helper(arr, start, end):

    # base case 1 element
    if start == end:
        return (arr[start], start, end)
    # divide by 2
    mid = (start + end) // 2

    # Recursive
    left_result = helper(arr, start, mid)
    right_result = helper(arr, mid + 1, end)

    # Enumeration,theta n^2
    # placeholder for cross_result(sum,mid,mid+1 since its mid)
    best_cross_sum = float("inf")
    best_cross_start = mid
    best_cross_end = mid + 1
    left_sum = 0

    for i in range(mid, start - 1, -1):
        # walk backward from mid to left
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


# The Algorithm 3
def algorithm3(arr):
    if len(arr) == 0:
        return None
    best_sum, start, end = helper(arr, 0, len(arr) - 1)
    return best_sum, arr[start : end + 1]


if __name__ == "__main__":

    # time take for 100-900, average from 10 tries
    for size in range(100, 1000, 100):
        total_time = 0
        for i in range(10):
            arr = gen_array(size)
            clock_start = time.time()
            algorithm3(arr)
            clock_end = time.time()
            elapsed_time = clock_end - clock_start
            total_time += elapsed_time
        # average of 10 runs
        average_time = total_time / 10
        print(average_time)
    #     # time take for 1000-9000, average from 10 tries
    for size in range(1000, 10000, 1000):
        total_time = 0
        for i in range(10):
            arr = gen_array(size)
            clock_start = time.time()
            algorithm3(arr)
            clock_end = time.time()
            elapsed_time = clock_end - clock_start
            total_time += elapsed_time
        average_time = total_time / 10
        print(average_time)