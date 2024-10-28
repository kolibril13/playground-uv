# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "numpy==2.1.2",
#     "pandas==2.2.3",
# ]
# ///

import marimo

__generated_with = "0.9.6"
app = marimo.App(width="medium")


@app.cell
def __():
    import pandas
    return (pandas,)


@app.cell
def __():
    import numpy
    numpy.rad2deg(3.14)
    return (numpy,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()


