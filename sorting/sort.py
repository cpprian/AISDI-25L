import random
from typing import List


def bubble_sort(input: List[str]) -> List[str]:
    n = len(input)
    for i in range(n):
        is_sorted = True
        for j in range(n - 1):
            if input[j] > input[j + 1]:
                is_sorted = False
                input[j], input[j + 1] = input[j + 1], input[j]

        if is_sorted:
            break


def insertion_sort(input: List[str]) -> List[str]:
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and input[j] > key:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = key


def selection_sort(input: List[str]) -> List[str]:
    n = len(input)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if input[j] < input[min_idx]:
                min_idx = j
        input[i], input[min_idx] = input[min_idx], input[i]


def merge(left: List[str], right: List[str]) -> List[str]:
    nl = len(left)
    nr = len(right)
    output = [None] * (nl + nr)
    i = j = k = 0
    while i < nl and j < nr:
        if left[i] < right[j]:
            output[k] = left[i]
            i += 1
        else:
            output[k] = right[j]
            j += 1
        k += 1

    for m in range(i, nl):
        output[k] = left[m]
        k += 1

    for m in range(j, nr):
        output[k] = right[m]
        k += 1
    return output


def merge_sort_helper(input: List[str], _from: int, _to: int) -> List[str]:
    if _from < _to:
        mid = (_from + _to) // 2
        left = input[_from : mid + 1]
        right = input[mid + 1 : _to + 1]
        merge_sort_helper(left, 0, len(left) - 1)
        merge_sort_helper(right, 0, len(right) - 1)
        output = merge(left, right)
        for i in range(len(output)):
            input[_from + i] = output[i]


def merge_sort(input: List[str]):
    merge_sort_helper(input, 0, len(input) - 1)


def partition(input: List[str], low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    input[pivot_index], input[high] = input[high], input[pivot_index]
    pivot = input[high]

    i = low - 1
    for j in range(low, high):
        if input[j] < pivot:
            i += 1
            input[i], input[j] = input[j], input[i]

    input[i + 1], input[high] = input[high], input[i + 1]
    return i + 1


def quick_sort_helper(input: List[str], low: int, high: int):
    if low < high:
        pivot = partition(input, low, high)
        quick_sort_helper(input, low, pivot - 1)
        quick_sort_helper(input, pivot + 1, high)


def quick_sort(input: List[str]):
    quick_sort_helper(input, 0, len(input) - 1)
