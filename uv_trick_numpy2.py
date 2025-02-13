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


Env("numpy==1.26.4", python="3.11").run(uses_numpy)
Env("numpy==2.2.2" , python="3.11").run(uses_numpy)
