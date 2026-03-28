"""
Demonstration: GIL impact on CPU-bound multithreading in Python.

Run this file to see:
1. Sequential execution (baseline)
2. Threaded execution (GIL bottleneck - no speedup)
3. Multiprocessing execution (bypasses GIL - real speedup)
4. Async I/O-bound demo (GIL released during I/O - speedup)
"""

import time
import threading
import multiprocessing
import concurrent.futures
import os


# ============================================================
# CPU-BOUND TASK (GIL prevents true parallelism with threads)
# ============================================================
def cpu_bound_task(n: int = 30_000_000) -> float:
    """Pure CPU work — counting. GIL is NOT released here."""
    total = 0
    for i in range(n):
        total += i * i
    return total


# ============================================================
# I/O-BOUND TASK (GIL IS released during I/O waits)
# ============================================================
def io_bound_task(seconds: float = 1.0) -> str:
    """Simulated I/O — time.sleep releases the GIL."""
    time.sleep(seconds)
    return f"Slept {seconds}s on PID={os.getpid()}, TID={threading.current_thread().name}"


# ============================================================
# BENCHMARKS
# ============================================================
NUM_WORKERS = 4
CPU_WORK = 10_000_000  # reduced so it finishes in reasonable time


def benchmark_sequential_cpu():
    """Run CPU tasks one after another."""
    print("\n" + "=" * 60)
    print("1️⃣  SEQUENTIAL CPU-BOUND (baseline)")
    print("=" * 60)

    start = time.perf_counter()
    results = [cpu_bound_task(CPU_WORK) for _ in range(NUM_WORKERS)]
    elapsed = time.perf_counter() - start

    print(f"   Tasks: {NUM_WORKERS}")
    print(f"   Time:  {elapsed:.3f}s")
    return elapsed


def benchmark_threaded_cpu():
    """
    Run CPU tasks with threads.
    GIL prevents true parallelism → expect ~same time as sequential.
    """
    print("\n" + "=" * 60)
    print("2️⃣  THREADED CPU-BOUND (GIL bottleneck)")
    print("=" * 60)

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(cpu_bound_task, CPU_WORK) for _ in range(NUM_WORKERS)]
        results = [f.result() for f in futures]
    elapsed = time.perf_counter() - start

    print(f"   Tasks:   {NUM_WORKERS}")
    print(f"   Threads: {NUM_WORKERS}")
    print(f"   Time:    {elapsed:.3f}s")
    print("   ⚠️  Notice: similar or SLOWER than sequential (GIL contention)")
    return elapsed


def benchmark_multiprocess_cpu():
    """
    Run CPU tasks with processes.
    Each process has its OWN GIL → true parallelism → real speedup.
    """
    print("\n" + "=" * 60)
    print("3️⃣  MULTIPROCESSING CPU-BOUND (bypasses GIL) ✅")
    print("=" * 60)

    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(cpu_bound_task, CPU_WORK) for _ in range(NUM_WORKERS)]
        results = [f.result() for f in futures]
    elapsed = time.perf_counter() - start

    print(f"   Tasks:     {NUM_WORKERS}")
    print(f"   Processes: {NUM_WORKERS}")
    print(f"   Time:      {elapsed:.3f}s")
    print("   ✅ Notice: significantly FASTER (each process has own GIL)")
    return elapsed


def benchmark_threaded_io():
    """
    Run I/O tasks with threads.
    GIL IS released during I/O → threads work great here.
    """
    print("\n" + "=" * 60)
    print("4️⃣  THREADED I/O-BOUND (GIL released during sleep/IO) ✅")
    print("=" * 60)

    # Sequential I/O first
    start = time.perf_counter()
    for _ in range(NUM_WORKERS):
        io_bound_task(1.0)
    seq_elapsed = time.perf_counter() - start
    print(f"   Sequential: {seq_elapsed:.3f}s")

    # Threaded I/O
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(io_bound_task, 1.0) for _ in range(NUM_WORKERS)]
        results = [f.result() for f in futures]
    thr_elapsed = time.perf_counter() - start
    print(f"   Threaded:   {thr_elapsed:.3f}s")
    print(f"   ✅ Speedup: {seq_elapsed / thr_elapsed:.1f}x (GIL released during I/O)")
    return seq_elapsed, thr_elapsed


# ============================================================
# C-EXTENSION EXAMPLE: NumPy releases GIL during computation
# ============================================================
def benchmark_numpy_gil_release():
    """
    NumPy releases the GIL during heavy array operations.
    This means threads CAN run NumPy in parallel.
    """
    try:
        import numpy as np
    except ImportError:
        print("\n" + "=" * 60)
        print("5️⃣  NUMPY GIL RELEASE (skipped — numpy not installed)")
        print("=" * 60)
        print("   Install with: pip install numpy")
        return None

    print("\n" + "=" * 60)
    print("5️⃣  NUMPY GIL RELEASE (C-extensions release GIL) ✅")
    print("=" * 60)

    def numpy_work():
        """NumPy internally releases GIL for C-level computation."""
        a = np.random.rand(2000, 2000)
        b = np.random.rand(2000, 2000)
        return np.dot(a, b)

    # Sequential
    start = time.perf_counter()
    for _ in range(NUM_WORKERS):
        numpy_work()
    seq_elapsed = time.perf_counter() - start
    print(f"   Sequential: {seq_elapsed:.3f}s")

    # Threaded
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(numpy_work) for _ in range(NUM_WORKERS)]
        [f.result() for f in futures]
    thr_elapsed = time.perf_counter() - start
    print(f"   Threaded:   {thr_elapsed:.3f}s")
    print(f"   ✅ Speedup: {seq_elapsed / thr_elapsed:.1f}x (NumPy releases GIL in C)")


# ============================================================
# MANUAL GIL RELEASE via ctypes (advanced demo)
# ============================================================
def benchmark_ctypes_gil_release():
    """
    Demonstrate releasing GIL by calling C library functions via ctypes.
    libc's usleep() releases the GIL automatically.
    """
    import ctypes
    import ctypes.util
    import platform

    print("\n" + "=" * 60)
    print("6️⃣  CTYPES GIL RELEASE (calling C library releases GIL)")
    print("=" * 60)

    if platform.system() == "Darwin":
        libc = ctypes.CDLL("libSystem.B.dylib")
    elif platform.system() == "Linux":
        libc_path = ctypes.util.find_library("c")
        libc = ctypes.CDLL(libc_path)
    else:
        print("   Skipped on this platform")
        return

    def c_sleep():
        """usleep(500000) = 0.5s — GIL is released during this C call."""
        libc.usleep(500_000)  # microseconds

    # Sequential
    start = time.perf_counter()
    for _ in range(NUM_WORKERS):
        c_sleep()
    seq_elapsed = time.perf_counter() - start
    print(f"   Sequential: {seq_elapsed:.3f}s")

    # Threaded
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(c_sleep) for _ in range(NUM_WORKERS)]
        [f.result() for f in futures]
    thr_elapsed = time.perf_counter() - start
    print(f"   Threaded:   {thr_elapsed:.3f}s")
    print(f"   ✅ Speedup: {seq_elapsed / thr_elapsed:.1f}x (C call releases GIL)")


# ============================================================
# SUMMARY
# ============================================================
def print_summary(seq_time, thr_time, mp_time):
    print("\n" + "=" * 60)
    print("📊 SUMMARY — CPU-BOUND WORK")
    print("=" * 60)
    print(f"   Sequential:     {seq_time:.3f}s (baseline)")
    print(f"   Threaded:       {thr_time:.3f}s (GIL → ~{seq_time/thr_time:.1f}x)")
    print(f"   Multiprocess:   {mp_time:.3f}s (no GIL → ~{seq_time/mp_time:.1f}x)")
    print()
    print("   🔴 Threads + CPU-bound = NO speedup (GIL held)")
    print("   🟢 Processes + CPU-bound = REAL speedup (separate GILs)")
    print("   🟢 Threads + I/O-bound = REAL speedup (GIL released)")
    print("   🟢 Threads + C-extensions (NumPy) = REAL speedup (GIL released in C)")
    print()
    print(f"   Python version: {os.sys.version}")
    print(f"   CPU cores: {multiprocessing.cpu_count()}")
    print("=" * 60)


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("🐍 Python GIL Demonstration")
    print(f"   Python: {os.sys.version}")
    print(f"   CPUs:   {multiprocessing.cpu_count()}")
    print(f"   PID:    {os.getpid()}")

    seq = benchmark_sequential_cpu()
    thr = benchmark_threaded_cpu()
    mp = benchmark_multiprocess_cpu()

    benchmark_threaded_io()
    benchmark_numpy_gil_release()
    benchmark_ctypes_gil_release()

    print_summary(seq, thr, mp)