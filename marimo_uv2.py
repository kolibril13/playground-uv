# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.2.3",
#     "polars==1.9.0",
# ]
# ///

import marimo

__generated_with = "0.9.4"
app = marimo.App(width="medium")


@app.cell
def __():
    import pandas as pd
    import polars
    return pd, polars


@app.cell
def __(pd):
    pd.DataFrame()
    return


@app.cell
def __():
    import marimo as mo

    def simple_red_dot(messages, config):
        return mo.md("![example](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==)"
    )


    mo.ui.chat(
        simple_red_dot,
    )
    return mo, simple_red_dot


@app.cell
def __():
    return


@app.cell
def __(mo):
    mo.md("hello![example](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==) world")
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
