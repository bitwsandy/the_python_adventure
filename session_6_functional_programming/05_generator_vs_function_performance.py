import sys
import time
import tracemalloc


# ---------------------------------------------
# NORMAL FUNCTION (RETURN) → builds full list
# ---------------------------------------------
def create_list(n):
    return [i for i in range(n)]


# ---------------------------------------------
# GENERATOR FUNCTION (YIELD) → one by one
# ---------------------------------------------
def create_generator(n):
    for i in range(n):
        yield i


# ---------------------------------------------
# MEMORY + TIME DEMO
# ---------------------------------------------
def demo(n):
    print(f"\nTesting with N = {n:,}\n")

    # ---------- LIST VERSION ----------
    tracemalloc.start()
    start = time.time()

    numbers_list = create_list(n)

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("LIST VERSION (return)")
    print(f"Time taken: {end - start:.2f} sec")
    print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
    print("-" * 40)

    # free memory
    del numbers_list
    time.sleep(1)

    # ---------- GENERATOR VERSION ----------
    tracemalloc.start()
    start = time.time()

    numbers_gen = create_generator(n)

    # only create generator object (no full load)
    mid = time.time()
    current, peak = tracemalloc.get_traced_memory()

    print("GENERATOR VERSION (yield)")
    print(f"Time to create generator object: {mid - start:.5f} sec")
    print(f"Memory after creation: {peak / 1024 / 1024:.5f} MB")

    # Now actually process all numbers (simulate pipeline)
    total = 0
    for num in numbers_gen:
        total += num

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time to iterate all values: {end - mid:.2f} sec")
    print(f"Peak memory during iteration: {peak / 1024 / 1024:.2f} MB")
    print("-" * 40)


# ---------------------------------------------
# RUN
# ---------------------------------------------
if __name__ == "__main__":
    demo(5_000_000)  # increase if RAM allows
