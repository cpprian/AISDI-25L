import copy
from sort import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort
from utils import (
    load_data,
    count_time,
    make_figure_comparing_time,
    make_figure_comparing_all,
)


if __name__ == "__main__":
    filename = "pan-tadeusz-unix.txt"
    space = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    n = len(space)

    data = load_data(filename, n, space)
    data_bubble = copy.deepcopy(data)
    data_insertion = copy.deepcopy(data)
    data_selection = copy.deepcopy(data)
    data_merge = copy.deepcopy(data)
    data_quick = copy.deepcopy(data)

    time_bubble = [None] * n
    time_insertion = [None] * n
    time_selection = [None] * n
    time_merge = [None] * n
    time_quick = [None] * n
    for i in range(n):
        time_bubble[i] = count_time(bubble_sort, data_bubble[i])
        time_insertion[i] = count_time(insertion_sort, data_insertion[i])
        time_selection[i] = count_time(selection_sort, data_selection[i])
        time_merge[i] = count_time(merge_sort, data_merge[i])
        time_quick[i] = count_time(quick_sort, data_quick[i])

    make_figure_comparing_all(
        space,
        "Bubble vs Insertion vs Selection sort",
        ["Bubble", "Insertion", "Selection"],
        time_bubble,
        time_insertion,
        time_selection,
    )
    make_figure_comparing_all(
        space,
        "Merge vs Quick sort",
        ["Merge", "Quick"],
        time_merge,
        time_quick,
    )
    make_figure_comparing_all(
        space,
        "All sorting algorithms",
        ["Bubble", "Insertion", "Selection", "Merge", "Quick"],
        time_bubble,
        time_insertion,
        time_selection,
        time_merge,
        time_quick,
    )
