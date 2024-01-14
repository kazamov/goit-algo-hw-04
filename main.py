import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

if __name__ == "__main__":
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]

    time_insertion_small = timeit.timeit(
        lambda: insertion_sort(data_small[:]), number=10
    )
    time_merge_small = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_timsort_small = timeit.timeit(lambda: sorted(data_small[:]), number=10)

    time_insertion_medium = timeit.timeit(
        lambda: insertion_sort(data_medium[:]), number=10
    )
    time_merge_medium = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_timsort_medium = timeit.timeit(lambda: sorted(data_medium[:]), number=10)

    print(
        f"{'|Alogrithm': <20} | {'Time small data': <20} | {'Time medium data': <20}|"
    )
    print(f"|{'-'*20} | {'-'*20} | {'-'*20}|")
    print(
        f"{'|Insertion sort': <20} | {time_insertion_small: <20.5f} | {time_insertion_medium: <20.5f}|"
    )
    print(
        f"{'|Merge sort': <20} | {time_merge_small: <20.5f} | {time_merge_medium: <20.5f}|"
    )
    print(
        f"{'|Tim sort': <20} | {time_timsort_small: <20.5f} | {time_timsort_medium: <20.5f}|"
    )
    print(f"|{'-'*20} | {'-'*20} | {'-'*20}|")

    print(
        f"\n\nInsertion sort is {time_insertion_small / time_timsort_small:.2f} times slower than Tim sort for small data"
    )
    print(
        f"Insertion sort is {time_insertion_medium / time_timsort_medium:.2f} times slower than Tim sort for medium data"
    )

    print(
        f"\n\nMerge sort is {time_merge_small / time_timsort_small:.2f} times slower than Tim sort for small data"
    )
    print(
        f"Merge sort is {time_merge_medium / time_timsort_medium:.2f} times slower than Tim sort for medium data"
    )
