from typing import List
from sort import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort
from utils import read_words
import copy


def load_data(filename: str, times: int, space: List[int]) -> List[List[str]]:
    output = [None] * times
    for i in range(times):
        output[i] = read_words(filename, space[i])
    return output


def test_sorting():
    filename = "pan-tadeusz-unix.txt"
    space = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    data = load_data(filename, len(space), space)
    data_bubble = copy.deepcopy(data)
    data_insertion = copy.deepcopy(data)
    data_selection = copy.deepcopy(data)
    data_merge = copy.deepcopy(data)
    data_quick = copy.deepcopy(data)

    for i in range(len(space)):
        verify = sorted(data[i])
        bubble_sort(data_bubble[i])
        insertion_sort(data_insertion[i])
        selection_sort(data_selection[i])
        quick_sort(data_quick[i])

        assert verify == data_bubble[i]
        assert verify == data_insertion[i]
        assert verify == data_selection[i]
        assert verify == merge_sort(data_merge[i], 0, len(data_merge[i]))
        assert verify == data_quick[i]
