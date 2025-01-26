# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "uvtrick",
# ]
# ///

from uvtrick import Env

def uses_numpy():
    from importlib import metadata
    version = metadata.version("numpy")
    print(f"hello from numpy=={version}")

for version in ("1.26.4", "2.2.2"):
    Env(f"numpy=={version}", python="3.11").run(uses_numpy)
