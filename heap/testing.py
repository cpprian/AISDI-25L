import pytest
import random
from heap import DHeap

@pytest.fixture(scope="module")
def input_data():
    return [random.randint(1, 300000) for _ in range(100000)]

@pytest.mark.parametrize("d", [2, 5, 7])
def test_heap_correctness(d):
    heap = DHeap(d)
    input_data = [random.randint(1, 300000) for _ in range(10000)]
    
    for v in input_data:
        heap.append(v)

    sorted_data = sorted(input_data)
    for i in range(len(sorted_data)):
        assert heap.pop() == sorted_data[i]

@pytest.mark.benchmark(group="append")
@pytest.mark.parametrize("d", [2, 5, 7])
def test_benchmark_append(d, benchmark, input_data):
    def setup():
        heap = DHeap(d)
        return (heap,), {}

    def append_all(h: DHeap):
        for v in input_data:
            h.append(v)

    benchmark.pedantic(append_all, setup=setup, rounds=10)


@pytest.mark.benchmark(group="pop")
@pytest.mark.parametrize("d", [2, 5, 7])
def test_benchmark_pop(d, benchmark, input_data):
    def setup():
        heap = DHeap(d)
        for v in input_data:
            heap.append(v)
        
        return (heap,), {}

    def remove_all(h: DHeap):
        for _ in range(10000):
            h.pop()

    benchmark.pedantic(remove_all, setup=setup, rounds=10)