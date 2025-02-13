# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "uvtrick",
# ]
# ///

from uvtrick import Env

def benchmark():
    import time
    import sys
    version = sys.version_info
    print(f"Running benchmark with Python {version.major}.{version.minor}")

    total = 0
    N = 200_000_000
    start = time.time()
    for i in range(N):
        total = total+i

    duration = time.time() - start
    print(f"Adding {N} elements took {duration:.2f} seconds.\n")

print("Starting benchmark tests:")
Env(python="3.11").run(benchmark)
Env(python="3.12").run(benchmark)
Env(python="3.13").run(benchmark)
Env(python="3.14").run(benchmark)


