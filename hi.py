# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib==3.9.2",
#     "polars==1.9.0",
# ]
# ///

import marimo

__generated_with = "0.9.8"
app = marimo.App(width="medium")


@app.cell
def __():
    import sys
    print(sys.version)
    return (sys,)


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.__version__
    return


@app.cell
def __():
    print("hi")
    return


@app.cell
def __():
    import polars
    return (polars,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
