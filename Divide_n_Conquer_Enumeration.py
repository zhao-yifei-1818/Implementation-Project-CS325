import random


def gen_array(size):
    arr = []

    for i in range(size):
        num = random.randint(-100, 100)
        arr.append(num)

    return arr


def get_size():
    size = int(input("Enter array size: "))
    return size


def close_to_zero(arr):

    if len(arr) == 0:
        return None

    def solve(left, right):

        if left == right:
            return (
                arr[left],
                left,
                right
            )

        mid = (left + right) // 2

        left_answer = solve(left, mid)
        right_answer = solve(mid + 1, right)

        left_suffixes = []

        running_sum = 0

        for i in range(mid, left - 1, -1):

            running_sum += arr[i]

            left_suffixes.append(
                (running_sum, i)
            )

        right_prefixes = []

        running_sum = 0

        for j in range(mid + 1, right + 1):

            running_sum += arr[j]

            right_prefixes.append(
                (running_sum, j)
            )

        best_cross_sum = float("inf")
        best_cross_start = None
        best_cross_end = None

        for left_sum, left_start in left_suffixes:

            for right_sum, right_end in right_prefixes:

                total = left_sum + right_sum

                if abs(total) < abs(best_cross_sum):

                    best_cross_sum = total
                    best_cross_start = left_start
                    best_cross_end = right_end

        cross_answer = (
            best_cross_sum,
            best_cross_start,
            best_cross_end
        )

        best_answer = left_answer

        if abs(right_answer[0]) < abs(best_answer[0]):
            best_answer = right_answer

        if abs(cross_answer[0]) < abs(best_answer[0]):
            best_answer = cross_answer

        return best_answer

    best_sum, start, end = solve(0, len(arr) - 1)

    subarray = arr[start:end + 1]

    return best_sum, subarray


if __name__ == "__main__":

    size = get_size()

    a = gen_array(size)

    result = close_to_zero(a)

    print("\nOriginal Array:")
    print(a)

    print("\nClosest To Zero Result:")
    print(result)