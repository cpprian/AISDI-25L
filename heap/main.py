from heap import DHeap
from random import randint


def main():
    dimm = [2, 5, 7]
    for d in dimm:
        heap = DHeap(d)
        print(f"Heap with d = {d}")
        for i in range(100):
            heap.append(randint(1, 100))
        heap.display()
        print("\n")

if __name__ == "__main__":
    main()
