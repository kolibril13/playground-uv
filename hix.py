# /// script
# title = "UV togtether with typer"
# author = "Jan-Hendrik Müller"
# license = "MIT"
# version = "0.0.3"
# classifiers = [
#     "License :: OSI Approved :: MIT License",
#     "Programming Language :: Python :: 3.12",
#     "Topic :: Scientific/Engineering :: Visualization",
# ]
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
# ]
# ///

import typer
from typing import Optional

def main(
    my_message: Optional[str] = typer.Argument(None)
):
    print("Hello World", my_message)


if __name__ == "__main__":
    typer.run(main)






# /// script
# title = "UV togtether with typer"
# author = "Jan-Hendrik Müller"
# license = "MIT"
# version = "0.0.3"
# classifiers = [
#     "License :: OSI Approved :: MIT License",
#     "Programming Language :: Python :: 3.12",
#     "Topic :: Scientific/Engineering :: Visualization",
# ]
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
# ]
# ///

import typer
from typing import Optional

def main(
    my_message: Optional[str] = typer.Argument(None)
):
    print("Hello World", my_message)


if __name__ == "__main__":
    typer.run(main)






