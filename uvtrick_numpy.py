
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "uvtrick",
# ]
# ///

from uvtrick import Env

def benchmark():
    import time
    import numpy as np
    import sys
    version = sys.version_info
    print(f"Running benchmark with numpy=={np.__version__} and Python {version.major}.{version.minor}")

    N = 9000
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    start = time.time()
    C = np.dot(A, B)
    duration = time.time() - start
    print(f"Multiplying two {N}x{N} matrices took {duration:.2f} s.\n")


print("Starting benchmark tests:")
Env("numpy==2.2.2", python="3.11").run(benchmark)
Env("numpy==2.2.2", python="3.12").run(benchmark)
Env("numpy==2.2.2", python="3.13").run(benchmark)
Env("numpy==2.2.2", python="3.14").run(benchmark)

