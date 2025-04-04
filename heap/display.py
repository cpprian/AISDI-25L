import json
import matplotlib.pyplot as plt

def plot_benchmark_results():
    with open('.benchmarks/Darwin-CPython-3.9-64bit/0001_benchmark_results.json') as f:
        benchmarks = json.load(f)['benchmarks']

    insert = sorted((b["fullname"], b["stats"]["mean"]) for b in benchmarks if "append" in b["fullname"])
    delete = sorted((b["fullname"], b["stats"]["mean"]) for b in benchmarks if "pop" in b["fullname"])

    plt.figure()
    plt.plot(*zip(*insert), label='Append')
    plt.ylabel("Avg time[s]")
    plt.xticks(rotation=30, ha='right')
    plt.title("Heap Append Performance")
    plt.legend()
    plt.tight_layout()
    plt.savefig("img/append_performance.png")

    plt.figure()
    plt.plot(*zip(*delete), label='Pop')
    plt.ylabel("Avg time[s]")
    plt.xticks(rotation=30, ha='right')
    plt.title("Heap Pop Performance")
    plt.legend()
    plt.tight_layout()
    plt.savefig("img/pop_performance.png")

    plt.close('all')

if __name__ == "__main__":
    plot_benchmark_results()
    print("Benchmark results plotted.")